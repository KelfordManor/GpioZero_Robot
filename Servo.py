# Use a button to control the servo between its minimum and maximum positions:

from gpiozero import Servo, Button

servo = Servo(17)
btn = Button(14)

while True:
    servo.min()
    btn.wait_for_press()
    servo.max()
    btn.wait_for_press()