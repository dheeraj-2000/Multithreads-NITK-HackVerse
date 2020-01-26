import RPi.GPIO as GPIO
import sys
sys.path.append('./picam')
import capture as pic


def detect():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)
    GPIO.setup(2, GPIO.OUT)
    while 1:
        if(GPIO.input(14) == False):
            print("Motion detected !!")
            #IO.output(3, True)
            #for i in range(10):
            print ("Clicking Pictures !!")
            pic.capture_images()
            print ("Pictures clicked !!")
            break
