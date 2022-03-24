import gc
import os
import moviepy.editor as mp

# process video
def processVideo(input_directory, output_directory, day, hour):
    print("preparing new hour..." + hour)
    video = getHour(input_directory + day + "/" + hour)
    video.write_videofile(output_directory + day + "_" + hour + ".mp4")
    del(video)
    gc.collect()

# combine all the minutes in an hour
def getHour(hour_directory):
    #print(hour_directory)
    os.chdir(hour_directory)
    minutes = os.listdir(hour_directory)
    clips = []
    for minute in minutes:
        if minute.endswith(".mp4"):
            try:
                clips.append(mp.VideoFileClip(minute))
            except:
                pass
    video = mp.concatenate_videoclips(clips, method='compose')
    gc.collect()
    return video