import explorerhat as eh
from time import sleep
from random import randint
def wheel(channel, event):
  duration = randint(1, 10)
  print(duration)
  eh.motor.one.forward(100)
  sleep(duration)
  eh.motor.one.stop()
 
eh.touch.one.pressed(wheel)
