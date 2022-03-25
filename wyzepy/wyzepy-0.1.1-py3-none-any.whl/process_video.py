import gc
import os
import moviepy.editor as mp

# process video
def processVideo(input_directory, output_directory, day, hour, start_min, end_min):
    print("preparing new hour..." + hour)
    video = getHour(input_directory + day + "/" + hour, start_min, end_min)
    video.write_videofile(output_directory + day + "_" + hour + ".mp4")
    del(video)
    gc.collect()
    print("completed processing video...")

# combine all the minutes in an hour
def getHour(hour_directory, start_min = 0, end_min = 59):
    #print(hour_directory)
    os.chdir(hour_directory)
    minutes = sorted(os.listdir(hour_directory))
    clips = []
    for minute in minutes[start_min:end_min]:
        if minute.endswith(".mp4"):
            try:
                clips.append(mp.VideoFileClip(minute))
            except:
                pass
    video = mp.concatenate_videoclips(clips, method='compose')
    gc.collect()
    return video


#getHour(
#    hour_directory = "/Volumes/WYZE/record/20220318/14/", 
#    start_min = 0,
#    end_min = 2)