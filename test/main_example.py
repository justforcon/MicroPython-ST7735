import os
os.listdir()

from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,17,18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK);
v = 0
tft.text((0, v), "Hello World! abcdefghijkl", TFT.RED, sysfont, 2, nowrap=False)