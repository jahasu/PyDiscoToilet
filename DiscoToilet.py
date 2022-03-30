from DmxPy import DmxPy
import RPi.GPIO as GPIO
import time
import pygame
import soco
import random
from soco.discovery import by_name


button_pin = 26
relay_1= 23
relay_2 = 24
running = False


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1, GPIO.OUT) #bathroom Lights
GPIO.setup(relay_2, GPIO.OUT) #dmx???
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.cleanup()

dmx = DmxPy('/dev/ttyUSB0')
pygame.mixer.init()

#soco setup
sonos = by_name("Bathroom")
print( sonos)



#simplifies gpio relay control
def set_relays(state):
    
    if state:
        
        
        GPIO.output(relay_1, GPIO.HIGH)  #room lights
        GPIO.output(relay_2, GPIO.LOW) #dmx
        GPIO.cleanup()
        time.sleep(0.2)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay_1, GPIO.OUT) #bathroom Lights
        GPIO.setup(relay_2, GPIO.OUT) #dmx???
        GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

       # time.sleep(1)
        print("relays set to " + str(state))
    else:
        #GPIO.output(relay_2, GPIO.HIGH)
        GPIO.output(relay_1, GPIO.LOW)
        print("relays set to " + str(state))


#settings to set the room back to non disco mode
#kills all music and resets dmx
def restore(): 
    dmx.blackout()
    dmx.render()
    set_relays(1)
    pygame.mixer.music.stop()
    #GPIO.cleanup()
    #todo:restore mic 

#allows switching and setting of dmx scenes
def set_dmx(scene): 
    if scene == 1:
        print("enable Scene1 dmx")
        dmx.setChannel(1, 255) #dimmer
        dmx.setChannel(2, 0)   #strobe
        dmx.setChannel(3, 255) #red
        dmx.setChannel(4, 255) #green
        dmx.setChannel(5, 255) #blue
        dmx.setChannel(6, 255) #rotate

        #Cage
        dmx.setChannel(7, 255)  #dimmer
        dmx.setChannel(8, 0)    #strobe
        dmx.setChannel(9, 255)  #red
        dmx.setChannel(10, 255) #green
        dmx.setChannel(11, 255) #blue
        dmx.setChannel(12, 255) #white
        dmx.setChannel(13, 255) #rotate

        #Middle Light
        dmx.setChannel(14, 255) #dimmer
        dmx.setChannel(15, 0)   #strobe
        dmx.setChannel(16, 255) #red
        dmx.setChannel(17, 255) #green
        dmx.setChannel(18, 255) #blue
        dmx.setChannel(19, 255) #yellow

        #Laser
        dmx.setChannel(20, 255) #laser r
        dmx.setChannel(21, 255) #laser g
        dmx.setChannel(22, 255) #animation & rotaion speed
        dmx.setChannel(23, 255) #???????
        #-------------------------------------------
        dmx.setChannel(30, 255) #dimmer   ball in the middle
        dmx.setChannel(31, 0)   #strobe
        dmx.setChannel(32, 255) #red  brokem
        dmx.setChannel(33, 0)   #green
        dmx.setChannel(34, 255) #blue  beoken
        dmx.setChannel(35, 255) #moon rotate
        dmx.setChannel(36, 255) #dimmer
        dmx.setChannel(37, 0)   #strobe
        dmx.setChannel(38, 255) #red
        dmx.setChannel(39, 0)   #green
        dmx.setChannel(40, 255) #blue
        dmx.setChannel(41, 0)   #yellow
        dmx.setChannel(42, 255) #laser r
        dmx.setChannel(43, 0)   #laser g
        dmx.setChannel(44, 255) #pan rotate
        #-------------------------------------------
        dmx.setChannel(60, 255) #dimmer ball on toilet
        dmx.setChannel(61, 0)   #strobe
        dmx.setChannel(62, 255) #red (Broken)
        dmx.setChannel(63, 0)   #green (Broken)
        dmx.setChannel(64, 255) #blue
        dmx.setChannel(65, 255) #moon rotate
        dmx.setChannel(66, 255) #dimmer
        dmx.setChannel(67, 0)   #strobe  bad
        dmx.setChannel(68, 255) #red
        dmx.setChannel(69, 0)   #green  stuck on
        dmx.setChannel(70, 255) #blue   stuck
        dmx.setChannel(71, 0)   #yellow  stuck
        dmx.setChannel(72, 0)   #laser r
        dmx.setChannel(73, 0)   #laser g
        dmx.setChannel(74, 0)   #pan rotate
        dmx.render()
        
    if scene == 2: 
        print("enable Scene2 dmx")



#Runs the disco sequences
def set_state(scene):

    if random.randrange(10) == 1:
        scene = 3

    if scene == 1:
        print("scene 1")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/1.mp3')
        pygame.mixer.music.play(1)
        
    

    if scene == 2:
        print("scene 2")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/2.mp3')
        pygame.mixer.music.play(1)
    time.sleep(1)
    set_dmx(scene)
    
    if scene == 3:
        print("scene 3")
        pygame.mixer.music.load('/home/pi/Desktop/PyDiscoToilet/music/rick.mp3')
        pygame.mixer.music.play(1)
    time.sleep(1)
    set_dmx(1)
    
        

## while statement runs in a loop waiting for button press

restore()

while True: 
    
    time.sleep(0.05)
    if GPIO.input(button_pin) == 0: 

        if running:
            #stop running the shit 
            time.sleep(0.1)
            running = False
            restore()
            sonos.volume = sonosVol
            

        else:
            #run all the shit 
            sonosVol = sonos.volume
            sonos.volume = 0
            print("sonos vol saved " + str(sonosVol))
            #get current sonos vol
            set_relays(0)
            time.sleep(0.3)
            running = True
            
            set_state(1)
            #button pressed 

print('Stopping')
