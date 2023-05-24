import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_ILI9341 as TFT

# Raspberry Pi configuration:
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

# TFT display configuration:
TFT_WIDTH = 128
TFT_HEIGHT = 160

# Create TFT LCD display instance.
spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000)
display = TFT.ILI9341(DC, rst=RST, spi=spi, width=TFT_WIDTH, height=TFT_HEIGHT)

# Initialize display.
display.begin()
display.clear()

# Set text color and size.
text_color = TFT.WHITE
text_size = 2

# Set text position.
text_x = 10
text_y = 10

# Display the text.
display.draw_text(text_x, text_y, 'Hello, world!', text_color, text_size)
display.display()
