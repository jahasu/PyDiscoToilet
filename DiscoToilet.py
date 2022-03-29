from DmxPy import DmxPy
import RPi.GPIO as GPIO
import time

button_pin = 3
light_r= 23
dmx_r = 24

GPIO.setup(light_r, GPIO.OUT)
GPIO.setup(dmx_r, GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

dmx = DmxPy('/dev/ttyUSB0')

def rest_lights():
    dmx.blackout()
    dmx.render()

def turn_on_lights(scene):
    //turn on lights based on numebr of taps 
    if scene == 1:
    if scene == 2:

while True:
    if GPIO.input(button_pin) == 0 :
        print("Pin High")
        turn_on_lights(1)
    else:
        print("looping")


print('Stopping')
