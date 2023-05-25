from flask import Flask, request
from gpiozero import LED

led1 = LED(22)
led2 = LED(27)
led3 = LED(17)
led4 = LED(18)


def TurnON(number):
    if(number == 1):
        led1.on()
        led2.on()
        led3.on()
        led4.on()
    else:
        led1.off()
        led2.off()
        led3.off()
        led4.off()

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
