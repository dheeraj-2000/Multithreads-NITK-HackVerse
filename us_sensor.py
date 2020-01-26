import RPi.GPIO as GPIO
import time

def flee_animals ():

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG = 18
    ECHO = 24
    buzzer = 23
    led = 2

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)

    while True:
        GPIO.output(TRIG, False)
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.01)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if(distance >=10):
            GPIO.output(led, GPIO.LOW)
            GPIO.output(buzzer, GPIO.LOW)
            print ("10 se jyadaa")
            return

        else:
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
            print ("10 se kam, Fleeing animal!!!")


