from guizero import App, TextBox, PushButton, Text
import explorerhat as eh

def start():
    start_button.disable()
    stop_button.enable()
    eh.output.one.on()


def stop():
    start_button.enable()
    stop_button.disable()
    eh.output.one.off()

app = App("LED Activator")
label = Text(app, text="Turn the LED on and off")
start_button = PushButton(app, command=start, text="start")
stop_button = PushButton(app, command=stop, text="stop", enabled=False)


app.display()
