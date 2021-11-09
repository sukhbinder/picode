import imageio as iio
import os
import glob
import datetime



def make_videos():
    now = datetime.datetime.now()
    files=  os.listdir()
    datestr = now.strftime("%m_%d_%Y_{0}")
    hour = now.hour - 1
    #for hour in range(6, 24):
    nowstr = datestr.format(str(hour).zfill(2))
    hours = [f for f in files if f.startswith(nowstr)]
    writer = iio.get_writer(r'/home/pi/Desktop/images/v_{}.mp4'.format(nowstr, fps=2))
    for im in hours:
        writer.append_data(iio.imread(im))
    writer.close()

if __name__ == "__main__":
    os.chdir(r"/home/pi/Desktop/images")
    make_videos()
