import explorerhat as eh

while True:
  
    x=eh.analog.one.read()
    
    percent = (x-2.6505)*35

    
    eh.motor.one.speed(percent)
