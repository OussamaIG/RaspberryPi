from flask import Flask, request
from gpiozero import LED
import time
import requests
from datetime import datetime
import pytz
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

led1 = LED(14)
led2 = LED(15)
led3 = LED(18)
led4 = LED(23)

light1 = False
light2 = False
light3 = False
light4 = False
toggle = False
weather = False
metime = False

def screendisplay(msg, msg2):
    WIDTH = 128
    HEIGHT = 160
    SPEED_HZ = 16000000

    MESSAGE = msg + msg2


# Raspberry Pi configuration.
    DC = 24
    RST = 25
    SPI_PORT = 0
    SPI_DEVICE = 0

# Create TFT LCD display class.
    disp = TFT.ST7735(
        DC,
        rst=RST,
        spi=SPI.SpiDev(
            SPI_PORT,
            SPI_DEVICE,
            max_speed_hz=SPEED_HZ))

# Initialize display.
    disp.begin()


    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)


    text_x = 30
    text_y = 30

    t_start = time.time()

    img = img.rotate(180).resize((WIDTH, HEIGHT))
    draw.text((text_x, text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)
    


def split_string(input_string):
    # Split the string using "/"
    split_list = input_string.split("/")
    
    return split_list

def get_weather(city):
    api_key = 'a250cee351bb47a0bb9170931232505'  # Replace with your WeatherAPI key
    base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}'
    
    try:
        response = requests.get(base_url, params={'q': city})
        data = response.json()
        
        if 'error' in data:
            print(f"Error: {data['error']['message']}")
        else:
            location = data['location']['name']
            condition = data['current']['condition']['text']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            
            weather = { "cityname" : {location}, "temp" : {temperature}, "humidity" : {humidity}}
            return weather
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_current_time(city, time_zone):
    # Get the current time in UTC
    current_time = datetime.now(pytz.utc)
    
    # Convert the UTC time to the specified time zone
    target_time_zone = pytz.timezone(time_zone)
    converted_time = current_time.astimezone(target_time_zone)
    
    # Format the converted time
    formatted_time = converted_time.strftime("%H:%M:%S")  # Hours:Minutes:Seconds
    
    # Log the current time in the specified city
    return {formatted_time}

def get_date():
    current_time = datetime.now()

    # Format the current time and date
    formatted_time = current_time.strftime("%H:%M:%S")  # Hours:Minutes:Seconds
    formatted_date = current_time.strftime("%Y-%m-%d")  # Year-Month-Day
    data = {"time" : formatted_time, "date" : formatted_date}
    return data

def TurnON(number):
    global light1, light2, light3, light4, toggle, weather, metime

    if number == "1":
        print('ON')
        led1.on()
        led2.on()
        led3.on()
        led4.on()
    elif number == "0":
        print('OFF')
        led1.off()
        led2.off()
        led3.off()
        led4.off()
    elif number == "6":
        light1 = not light1
        if light1 == True :
            print('LIGHT4 on')
            led4.on()
        else :
            print('LIGHT4 off')
            led4.off()
    elif number == "3":
        light2 = not light2
        if light2 == True :
            print('LIGHT1 on')
            led1.on()
        else :
            print('LIGHT1 off')
            led1.off()
    elif number == "4":
        light3 = not light3
        if light3 == True :
            print('LIGHT2 on')
            led2.on()
        else :
            print('LIGHT2 off')
            led2.off()
    elif number == "5":
        light4 = not light4
        if light4 == True :
            print('LIGHT3 on')
            led3.on()
        else :
            print('LIGHT3 off')
            led3.off()
    elif number == "7":   
        toggle = not toggle
        if toggle == True :
            while toggle == True :
                led1.on()
                time.sleep(0.5)
                led1.off()
                led2.on()
                time.sleep(0.5)
                led2.off()
                led3.on()
                time.sleep(0.5)
                led3.off()
                led4.on()
                time.sleep(0.5)
                led4.off()
        else :
            print('toggle off')         
    elif number == "10" :
        weather = True
    elif weather == True:
        weather = get_weather(number)
        print(weather)
        # screendisplay()

    elif number == "9" :
        metime = True
    elif metime == True :
        city = split_string(number)
        mytime = get_current_time(city[1], number)
        print(f"Current Time in {city[1]}: {mytime}")
        # screendisplay()
    elif number == "8" :
        datetime = get_date()
        print(f"Current Time: {datetime['time']}")
        print(f"Current Date: {datetime['date']}")
        screendisplay(datetime["date"], datetime["time"])
app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/button", methods=["POST"])
def handle_button():
    value = request.form.get("value")
    print("Received value:", value)
    TurnON(value)
    return "Success"

if __name__ == "__main__":
    app.run()
