import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7735 as st7735

# Raspberry Pi configuration:
CS_PIN = digitalio.DigitalInOut(board.CE0)
DC_PIN = digitalio.DigitalInOut(board.D25)
RESET_PIN = digitalio.DigitalInOut(board.D24)

# TFT display configuration:
TFT_WIDTH = 128
TFT_HEIGHT = 160

# Create TFT LCD display instance.
spi = board.SPI()
display = st7735.ST7735R(spi, cs=CS_PIN, dc=DC_PIN, rst=RESET_PIN, width=TFT_WIDTH, height=TFT_HEIGHT)

# Initialize display.
display.fill(st7735.BLACK)
display.rotation = 90

# Load font file.
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)

# Create image buffer.
image = Image.new('RGB', (TFT_WIDTH, TFT_HEIGHT), color=st7735.BLACK)
draw = ImageDraw.Draw(image)

# Set text color.
text_color = (255, 255, 255)

# Set text position.
text_x = 10
text_y = 10

# Draw the text.
draw.text((text_x, text_y), 'Hello, world!', font=font, fill=text_color)

# Display the image.
display.image(image)

# Pause to show the text.
time.sleep(5)
