import gpiozero  # GPIO Zero library
import time  # Time library


# File name: obstacle_avoiding_robot.py
# Code source (Matt-Timmons Brown): https://github.com/the-raspberry-pi-guy/raspirobots
# Date created: 5/28/2019
# Python version: 3.5.3
# Description: A robot that avoids objects
# using an HC-SR04 ultrasonic distance sensor.

# Assign the GPIO pin number to these variables.
TRIG = 23
ECHO = 24

# This sends out the signal to the object
trigger = gpiozero.OutputDevice(TRIG)

# This variable is an input that receives
# the signal reflected by the object
echo = gpiozero.DigitalInputDevice(ECHO)

# Create a Robot object that is attached to
# GPIO pins 17, 18, 22, and 27 (change to 7, 11, 13, 15) of the
# Raspberry Pi. These pins are inputs for the
# L293D motor controller.
# Objects have data and behavior that is
# predefined by the Robot class (i.e. blueprint)
# declared inside the GPIO Zero library.
# Change the order of the numbers inside
# the parentheses until you get the desired
# behavior.
robot = gpiozero.Robot(left=(7, 13), right=(11, 15), forward=(7, 15))


# Get the distance to the object
def get_distance(trigger, echo):
    # Send out a 10 microsecond pulse (ping)
    # from the trasmitter (TRIG)
    trigger.on()
    time.sleep(0.00001)
    trigger.off()

    # Start timer as soon as the reflected sound
    # wave is "heard" by the receiver (echo)
    while echo.is_active == False:
        pulse_start = time.time()  # Time of last LOW reading

    # Stop the timer one the reflected sound wave
    # is done pushing through the receiver (ECHO)
    # Wave duration is proportional to duration of travel
    # of the original pulse.
    while echo.is_active == True:
        pulse_end = time.time()  # Time of last HIGH reading

    pulse_duration = pulse_end - pulse_start

    # 34300 cm/s is the speed of sound
    distance = 34300 * (pulse_duration / 2)

    # Round distance to two decimal places
    round_distance = round(distance, 2)

    return (round_distance)


while True:
    distance_to_object = get_distance(trigger, echo)

    # Avoid objects less than 15 cm away
    if distance_to_object <= 15:
        robot.right()  # Right for
        time.sleep(0.25)  # 0.25 seconds
    else:
        robot.forward()  # Forward for
        time.sleep(0.1)  # 0.1 seconds

# ====================================================================
# Make a robot with a distance sensor that runs away when things get within 20cm of it:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#servo
from gpiozero import Robot, DistanceSensor
from signal import pause

sensor = DistanceSensor(23, 24, max_distance=1, threshold_distance=0.2)
robot = Robot(left=(4, 14), right=(17, 18))

sensor.when_in_range = robot.backward
sensor.when_out_of_range = robot.stop
pause()