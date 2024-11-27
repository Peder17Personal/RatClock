import RPi.GPIO as GPIO
import time
from gpiozero import PWMOutputDevice


LED_RED = PWMOutputDevice(14)
LED_GREEN = PWMOutputDevice(15)
LED_BLUE = PWMOutputDevice(16)
human_detection = 21


#setup RGB at 255
LED_WHITE = {255, 255, 255}

#setup sun color
LED_SUN = {229, 115, 82}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setmode(human_detection, GPIO.IN)


def sunLightFunction(RGB_profile, lenght):
    