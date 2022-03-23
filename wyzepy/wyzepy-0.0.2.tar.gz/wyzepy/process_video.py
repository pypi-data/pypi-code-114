import gc
from get_hour import getHour
import moviepy.editor as mp

def processVideo(hour_directory, output_directory, day, hour):
    print("preparing new hour..." + hour)
    video = getHour(hour_directory + day + "/" + hour)
    video.write_videofile(output_directory + day + "_" + hour + ".mp4")
    del(video)
    gc.collect()