from gpiozero import Servo
from guizero import App, Box, Text, PushButton, Slider
from time import sleep

servo = Servo(26, 0, 0.0005, 0.0025)


def ServoPosition(slider_value):
    servo.value = int(slider_value) / 90



app = App(title="Servo GUI", width=350, height=150, layout="auto")

instruction_text = Text(app, text="Drag slider below to control servo position.")
servo_position = Slider(app, command=ServoPosition, start=-90, end=90, width='fill')

app.display()