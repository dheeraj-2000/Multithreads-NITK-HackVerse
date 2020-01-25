import us_sensor as us
import sys
sys.path.append ('./ir')
import  ir_detect as ir
sys.path.append ('./detection')
import detect

def main():

    print ("System ON !!")
    while 1:

        ir.detect()
        print("Detecting...")
        count = detect.detect_animals()
        if (count):
            print (count)
            us.flee_animals ()
        else:
            print ("NO ANIMAL !!")


if __name__ == "__main__":
    main()
