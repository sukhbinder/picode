from picamera import PiCamera
from time import sleep
from datetime import datetime

def capture_now(camera):
    now = datetime.now()
    nowstr = now.strftime("%m_%d_%Y_%H_%M_%S")
    camera.capture(r"/home/pi/Desktop/images/{}.png".format(nowstr))
    return None


now = datetime.now()
if now.hour >=  6 and now.hour < 23:
   camera = PiCamera()
   camera.start_preview()
   sleep(5)
   capture_now(camera)
   sleep(15)
   capture_now(camera)
   camera.stop_preview()
