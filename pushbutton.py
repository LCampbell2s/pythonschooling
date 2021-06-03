import explorerhat 
def push(input):
  state = input.read()
  if state == 1:
    print("you pushed me")
   else:
    print("you realeased me")

explorerhat.input.one.on_high(pushed)
explorerhat.input.one.on_low(released)
