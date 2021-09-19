# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import time  # import time module

# import picamera and datetime (to use in unique file naming)
from picamera import PiCamera
from datetime import datetime

# setup camera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = (25)

record = 0  # set up a variable to be set to 1 when recording
# set GPIO numbering mode and define output pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
# flashes LEDs when all running, and also lets camera settle
for x in range(1, 5):
    GPIO.output(29, False)
    time.sleep(0.5)
    GPIO.output(29, True)
    time.sleep(0.5)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        print(char)
        if char == ord('q'):
            break
        elif char == ord('r'):
            if record == 0:
                record = 1
                moment = datetime.now()
                GPIO.output(29, False)
                camera.start_recording(
                    '/home/pi/Videos/vid_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))
        elif char == ord('t'):
            if record == 1:
                record = 0
                GPIO.output(29, True)
                camera.stop_recording()

        elif char == curses.KEY_UP:
            print("up")
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)
        # we can replace curses.key with other any digits like this  ord('p'), ord('m') ..etc
        elif char == curses.KEY_DOWN:
            print("down")
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
        elif char == curses.KEY_RIGHT:
            print("right")
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)
        elif char == curses.KEY_LEFT:
            print("left")
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)

        else:
            print("stop")
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
camera.stop_recording()
GPIO.cleanup()
