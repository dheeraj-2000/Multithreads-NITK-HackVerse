import picamera

def capture_images ():
    for i in range (1,11):
        with picamera.PiCamera() as camera:
            camera.flash_mode = 'on'
            filename = "Picture" + str(i) +".jpg"
            camera.capture(filename)
