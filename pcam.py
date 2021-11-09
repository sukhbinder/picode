from picamera import PiCamera
from time import sleep
from datetime import datetime

now = datetime.now()
nowstr = now.strftime("%m_%d_%Y_%H_%M_%S")

if now.hour >  6 and now.hour < 23:
	camera = PiCamera()
	camera.start_preview()
	sleep(5)
	camera.capture(r"/home/pi/Desktop/images/{}.png".format(nowstr))
	camera.stop_preview()
