from DmxPy import DmxPy
import time

dmx = DmxPy('/dev/ttyUSB0')
print("hello")
dmx.setChannel(1,255)
dmx.setChannel(2, 255)
dmx.setChannel(3, 255)
dmx.setChannel(4, 0)
dmx.render()
time.sleep(2)
dmx.setChannel(5, 0)
time.sleep(2)
dmx.blackout()
dmx.render()