import os
import moviepy.editor as mp
import gc

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

#if __name__ == '__main__':
#    getHour(hour_directory)