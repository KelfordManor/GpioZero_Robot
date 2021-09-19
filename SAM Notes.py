# Use a button to control the servo between its minimum and maximum positions.
# And another button to start the program.

#import Servo and Button
from gpiozero import Servo, Button


#main program
def run():
    while True:
        servo.min()
        #LOW
        print('Speed = Low\n')
        btn0.wait_for_press()
        #MID
        servo.mid()
        print('Speed = Mid\n')
        btn0.wait_for_press()
        #MAX
        servo.max()
        print('Speed = High\n')
        btn0.wait_for_press()


#Set variables
servo = Servo(17)
btn0 = Button(14)

#Start Program w/Button
btn2 = Button(11, hold_time=2)
btn2.when_held = run
