import wave
import os
from formatConvert.wav_pcm import pcm2wav,wav2pcm
import  numpy as np
import math
from moviepy.editor import *



def get_wav_from_mp4(mp4file):
    """
    Parameters
    ----------
    mp4file

    Returns
    -------

    """
    suffix = os.path.splitext(mp4file)[-1]
    if suffix != '.mp4':
        raise TypeError('wrong format! not mp4 file!' + str(suffix))
    video = VideoFileClip(mp4file)
    audio = video.audio
    newFileName = mp4file[:-4] + '.wav'
    audio.write_audiofile(newFileName)
    return newFileName

def get_rms(records):
    '''
    Parameters
    ----------
    records

    Returns
    -------
    '''
    return math.sqrt(sum([x * x for x in records])/len(records))

def isSlience(Filename =None):
    """
    Parameters
    ----------
    Filename 支持 wav 和 pcm 和MP4

    Returns
    -------

    """
    suffix = os.path.splitext(Filename)[-1]
    if suffix == '.mp4':
        Filename = get_wav_from_mp4(Filename)
    with open(wav2pcm(Filename), 'rb') as ref:
        indata = ref.read()
    ins = np.frombuffer(indata, dtype=np.int16)
    print(ins)
    dBrmsValue = 20*math.log(get_rms(ins)/32767)
    return dBrmsValue
    pass


def audioFormat(wavFileName=None):
    """
    wavFileName：输入文件 wav，mp4
    Returns
    -------
    refChannel:通道数
    refsamWidth：比特位 2代表16bit
    refsamplerate：采样率
    refframeCount：样点数
    """
    suffix = os.path.splitext(wavFileName)[-1]
    if suffix != '.wav' or suffix != '.mp4':
        raise TypeError('wrong format! not wav/mp4 file!' + str(suffix))
    if suffix == '.mp4':
        wavFileName = get_wav_from_mp4(wavFileName)
    wavf = wave.open(wavFileName, 'rb')
    refChannel,refsamWidth,refsamplerate,refframeCount = wavf.getnchannels(),wavf.getsampwidth(),wavf.getframerate(),wavf.getnframes()
    return refChannel,refsamWidth,refsamplerate,refframeCount

if __name__ == '__main__':
    ref = r'C:\Users\vcloud_avl\Downloads\Speech\TestCase_01_None_None\near_cn\far_cn.wav'
    isSlience(ref)
    print(audioFormat(ref))