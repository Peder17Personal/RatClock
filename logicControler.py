import RPi.GPIO as GPIO
import time
from gpiozero import PWMOutputDevice

LED_RED = PWMOutputDevice(12)   #Physical pin 12
LED_GREEN = PWMOutputDevice(32) #Physical pin 32
LED_BLUE = PWMOutputDevice(33)  #Physical pin 33
human_detection_button = 21


#setup RGB at 255
LED_WHITE = {255, 255, 255} #Strongest white light

#Emergency light AKA Defcon 1
LED_DEFCON1 = {170, 15, 15} #Red emergency light

#setup sun color
LED_SUN = {229, 115, 82} #RGB values to emitate natural sunlight

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

GPIO.setmode(human_detection_button, GPIO.IN)


def LED_WHITE_LIGHT():
     #set LED light to 255 of all channels
     print("hete")

def sunLightFunction(RGB_profile, lenght):
    seconds = 0
    for seconds in lenght:
        print("Slowly increase sunlight")
        #Logic here
        seconds = seconds + 1


def HumanDetection():
     
     if GPIO.input(human_detection_button) == GPIO.LOW:
        print("Button pressed.")
        GPIO.output(LED_RED, GPIO.HIGH)
    else:
        print("Button released.")
        GPIO.output(LED_RED, GPIO.LOW)