import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
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

# Initialization 
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

#Functions
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

def screendisplay(msg, msg2):
    WIDTH = 128
    HEIGHT = 160
    SPEED_HZ = 16000000

    MESSAGE = msg


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

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)


    text_x = 20
    text_y = 30

    t_start = time.time()

    draw.text((text_x, text_y), MESSAGE, font=font, fill=(255, 255, 255))
    draw.text((text_x, text_y+60), msg2, font=font, fill=(255, 255, 255))
    disp.display(img)
    

# Fetch the service account key JSON file from Firebase console
cred = credentials.Certificate('C://Users//OUSSAMA//Documents//Master//S2//IOT//RaspberryPi//Lights//filejson.json')

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberrypi-d200d-default-rtdb.firebaseio.com/'
})

# Get a database reference
ref = db.reference('buttonValue')

# Retrieve the value of 'buttonValue'


# Log the value on the screen
while(True):
    button_value = ref.get()
    if button_value == 0:
        print('lights off')
        led1.off()
        led2.off()
        led3.off()
        led4.off()
    elif button_value == 1:
        print('lights on')
        led1.on()
        led2.on()
        led3.on()
        led4.on()
    elif button_value == 3:
        light2 = not light2
        if light2 == True :
            print('LIGHT1 on')
            led1.on()
        else :
            print('LIGHT1 off')
            led1.off()
    elif button_value == 4:
        light3 = not light3
        if light3 == True :
            print('LIGHT2 on')
            led2.on()
        else :
            print('LIGHT2 off')
            led2.off()
    elif button_value == 5:
        light4 = not light4
        if light4 == True :
            print('LIGHT3 on')
            led3.on()
        else :
            print('LIGHT3 off')
            led3.off()  
    elif button_value == 6:
        light1 = not light1
        if light1 == True :
            print('LIGHT4 on')
            led4.on()
        else :
            print('LIGHT4 off')
            led4.off()
    elif button_value == 7:
        toggle = not toggle
        if toggle == True :
            print('toggle on')
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
    elif button_value == 8:
        datetime = get_date()
        print(f"Current Time: {datetime['time']}")
        print(f"Current Date: {datetime['date']}")
        screendisplay(datetime["date"], datetime["time"])
    elif button_value == 9:
         metime = True
    elif metime == True :
        city = split_string(button_value)
        mytime = get_current_time(city[1], button_value)
        print(f"Current Time in {city[1]}: {mytime}")
        mytome = str(mytime)
        screendisplay(city[1], mytome)
        metime = False
    elif button_value == 10:
        weather = True
    elif weather == True:
        weather = get_weather(button_value)
        print(weather["cityname"], weather["temp"])
        screendisplay(str(weather["cityname"]), str(weather["temp"]))
        weather = False                      