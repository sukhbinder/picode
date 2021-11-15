import os
from  datetime import datetime


os.chdir(r"/home/pi/Desktop/images")

now = datetime.now()

today_png= now.strftime("%m_%d_%Y_*.png ")
cmdline = "mv "+today_png+r".backup/"
iret = os.system(cmdline)


