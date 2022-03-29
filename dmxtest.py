from DmxPy import DmxPy
import time

dmx = DmxPy('/dev/ttyUSB0')
print("hello")
dmx.setChannel(1, 100)
dmx.setChannel(2, 50)
dmx.setChannel(3, 50)
dmx.setChannel(4, 50)
dmx.render()
time.sleep(2)
dmx.setChannel(5, 100)
time.sleep(2)
dmx.blackout()
dmx.render()