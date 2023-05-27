from flask import Flask, request
from gpiozero import LED
import time

led1 = LED(22)
led2 = LED(27)
led3 = LED(17)
led4 = LED(18)

light1 = False
light2 = False
light3 = False
light4 = False
toggle = False

def TurnON(number):
    global light1, light2, light3, light4, toggle

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
            print('Toggle')
            led1.on()
            time.sleep(0.5)
            led2.on()
            time.sleep(0.5)
            led3.on()
            time.sleep(0.5)
            led4.on()
            time.sleep(0.5)
        else :
            print('toggle off')         

def turnonlight(number):
    match number:
        case 1:
            led1.on()
        case 2:
            led2.on()
        case 3 :
            led3.on()
        case 4 :
            led4.on()
    

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
