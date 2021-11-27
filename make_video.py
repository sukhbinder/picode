import imageio as iio
import os
import glob
import datetime



def make_videos():
    now = datetime.datetime.now()
    files=  os.listdir()
    files.sort(key =os.path.getmtime)
    datestr = now.strftime("%m_%d_%Y_{0}")
    hour = now.hour - 1
    #for hour in range(6, 24):
    nowstr = datestr.format(str(hour).zfill(2))
    hours = [f for f in files if f.startswith(nowstr)]
    writer = iio.get_writer(r'/home/pi/Desktop/images/v_{}.mp4'.format(nowstr, fps=2))
    for im in hours:
        try:
           writer.append_data(iio.imread(im))
        except Exception as ex:
           with open("error.txt" "w") as fout:
                fout.write("ERROR with \n{0}\n{1}".format(im, ex))
           continue
    writer.close()

def all_till_now():
    now = datetime.datetime.now()
    files = os.listdir()
    files.sort(key=os.path.getmtime)
    datestr = now.strftime("%m_%d_%Y_")
    files = [ f for f in files if f.endswith(".png")]
    fname = r"/home/pi/Desktop/images/v_{}_overval.mp4".format(datestr)
    writer = iio.get_writer(fname, fps=5)
    for im in files:
        try:
            writer.append_data(iio.imread(im))
        except Exception as ex:
            print(ex)
            continue
    writer.close()

if __name__ == "__main__":
    os.chdir(r"/home/pi/Desktop/images")
    make_videos()
    all_till_now()

