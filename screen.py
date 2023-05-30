from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time

import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


WIDTH = 128
HEIGHT = 160
SPEED_HZ = 16000000

MESSAGE = "Hello World! How are you today?"


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

size_x, size_y = draw.textsize(MESSAGE, font)

text_x = 10
text_y = 10

t_start = time.time()

draw.text((text_x, text_y), MESSAGE, font=font, fill=(255, 255, 255))
img = img.rotate(90).resize((WIDTH, HEIGHT))
disp.display(img)