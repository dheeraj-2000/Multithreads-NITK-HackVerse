import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(8, IO.IN)
IO.setup(3, IO.OUT)

while 1:
           if(IO.input(8) == False):
               print("Obstacle detected !!")
               IO.output(3, True)
           else:
               IO.output(3, False)
