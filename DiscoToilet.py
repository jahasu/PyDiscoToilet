from DmxPy import DmxPy
import RPi.GPIO as GPIO
import time
import pygame
import soco
from soco.discovery import by_name


button_pin = 26
relay_1= 23
relay_2 = 24
running = False
sonosVol = 10 
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1, GPIO.OUT)
GPIO.setup(relay_2, GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)

dmx = DmxPy('/dev/ttyUSB0')
pygame.mixer.init()

#soco setup
sonos = soco.by_name("Bathroom")
print("Sonos connected!" + sonos)



#simplifies gpio relay control
def set_relays(state): 
    if state:
        GPIO.output(relay_1, GPIO.LOW) #room lights on
        GPIO.output(relay_2, GPIO.HIGH)
    else:
        GPIO.output(relay_1, GPIO.HIGH)
        GPIO.output(relay_2, GPIO.LOW)


#settings to set the room back to non disco mode
#kills all music and resets dmx
def restore(): 
    dmx.blackout()
    dmx.render()
    set_relays(1)
    pygame.mixer.music.stop()
    set_relays(1)
    #todo:restore mic 

#allows switching and setting of dmx scenes
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



#Runs the disco sequences
def set_state(scene):

    set_dmx(scene)

    if scene == 1:
        print("scene 1")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/1.mp3')
        pygame.mixer.music.play(1)
        
        


    if scene == 2:
        print("scene 2")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/2.mp3')
        pygame.mixer.music.play(1)


## while statement runs in a loop waiting for button press

restore()

while True: 
    
    time.sleep(0.05)
    if GPIO.input(button_pin) == 0: 

        if running:
            #stop running the shit 
            time.sleep(1)
            running = False
            restore()
            sonos.volume = sonosVol
            

        else:
            #run all the shit 
            sonosVol = sonos.volume
            sonos.volume = 0
            #get current sonos vol
            set_relays(0)
            time.sleep(1)
            running = True
            set_state(2)
            #button pressed 

print('Stopping')
