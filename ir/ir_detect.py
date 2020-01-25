import RPi.GPIO as IO
import sys
sys.path.append('../picam')
import capture as pic
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(8, IO.IN)
IO.setup(3, IO.OUT)

while 1:
           if(IO.input(8) == False):
               print("Motion detected !!")
               #IO.output(3, True)
               #for i in range(10):
               print ("Clicking Pictures !!")
               pic.capture_images()
               print ("Pictures clicked !!")
           else:
               IO.output(3, False)
