from m5stack import *

import time
import unit

from terminal import Terminal
  
env0 = unit.get(unit.ENV, unit.PORTA)
 
t = Terminal()
while True:
  
  if btnA.wasPressed():
    break
  
  pressure = env0.pressure
  temperature = env0.temperature
  humidity = env0.humidity
    
  t.print("P={pressure}, T={temperature}, H={humidity}".format(
    pressure=pressure,
    temperature=temperature,
    humidity=humidity
  ))
  wait_ms(500)