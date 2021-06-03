import explorerhat as eh
import time

eh.output.one.on()
print("Lights on!")
time.sleep(2)
eh.output.one.off()
print("Lights out!")
