from DmxPy import DmxPy
import RPi.GPIO as GPIO
import time
import pygame

button_pin = 26
relay_1= 23
relay_2 = 24

running = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1), GPIO.OUT)
GPIO.setup(relay_2, GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

dmx = DmxPy('/dev/ttyUSB0')
pygame.mixer.init()

def restore():
    dmx.blackout()
    dmx.render()
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()


def set_dmx(scene):
    if scene == 1:
        print("enable Scene1 dmx")
        dmx.setChannel(1,255)
        dmx.setChannel(2, 255)
        dmx.setChannel(3, 255)
        dmx.setChannel(4, 0)
        dmx.render()
        
    if scene == 2: 
        print("enable Scene2 dmx")

def set_relays(state): #1 turns main lights on 
    if state:
        GPIO.output(relay_1, GPIO.LOW)
        GPIO.output(relay_2, GPIO.HIGH)
    else:
        GPIO.output(relay_1, GPIO.HIGH)
        GPIO.output(relay_2, GPIO.LOW)

def set_scene(scene):
    #kill lights 
    #delay an ammount 
    

    #turn on lights based on numebr of taps 
    set_lights(scene)

    if scene == 1:
        print("scene 1")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/1.mp3')
        pygame.mixer.music.play(1)
        
        


    if scene == 2:
        print("scene 2")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/1.mp3')
        pygame.mixer.music.play(1)


## while statement runs the code 
while True: 

    if GPIO.input(button_pin) == 0: 

        if running: 
            running = False
            restore()
            set_relays(1)

        else:
            restore()
            set_relays(0)
            running = True

            set_scene(2)
            #button pressed 




print('Stopping')
