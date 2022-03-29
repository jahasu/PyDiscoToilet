from DmxPy import DmxPy
import RPi.GPIO as GPIO
import time
import pygame

button_pin = 26
light_r= 23
dmx_r = 24

running = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(light_r, GPIO.OUT)
GPIO.setup(dmx_r, GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

dmx = DmxPy('/dev/ttyUSB0')
pygame.mixer.init()

def reset_lights():
    dmx.blackout()
    dmx.render()

def set_scene(scene):
  #turn on lights based on numebr of taps 
    if scene == 1:
        print("scene 1")
        pygame.mixer.music.play
        
        


    if scene == 2:
        print("scene 2")



while True:
    if running == 0 and GPIO.input(button_pin) == 1:
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/1.mp3')
        set_scene(1)
        #button pressed 




print('Stopping')
