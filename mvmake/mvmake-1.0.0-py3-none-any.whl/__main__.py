import typing
import glob
import os
import argparse

import librosa
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from tqdm import tqdm

from .sourceclip import SourceClip
from .videosize import VideoSize


EXTENSIONS = ['mp4', 'avi', 'mov']

BANNER = """
 ███▄ ▄███▓ ██▒   █▓ ███▄ ▄███▓ ▄▄▄       ██ ▄█▀▓█████ 
▓██▒▀█▀ ██▒▓██░   █▒▓██▒▀█▀ ██▒▒████▄     ██▄█▒ ▓█   ▀ 
▓██    ▓██░ ▓██  █▒░▓██    ▓██░▒██  ▀█▄  ▓███▄░ ▒███   
▒██    ▒██   ▒██ █░░▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ 
▒██▒   ░██▒   ▒▀█░  ▒██▒   ░██▒ ▓█   ▓██▒▒██▒ █▄░▒████▒
░ ▒░   ░  ░   ░ ▐░  ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░
░  ░      ░   ░ ░░  ░  ░      ░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░
░      ░        ░░  ░      ░     ░   ▒   ░ ░░ ░    ░   
       ░         ░         ░         ░  ░░  ░      ░  ░
                ░                                      
"""

def load_source_clips (
    path: str,
    target_resolution: VideoSize = (None, None),
    extensions: typing.List[str] = None
) -> typing.List[SourceClip]:
    clips = []
    files = []

    for filename in glob.iglob(path + '/**/**', recursive=True):
        if extensions == None:
            files.append(filename)
            continue

        file_extension = os.path.splitext(filename)[1][1:].strip().lower()
        if file_extension in extensions:
            files.append(filename)

    for f in tqdm(files):
        try:
            clips.append(SourceClip(f, target_resolution))
        except Exception as e:
            raise e
            pass

    return clips

def get_beat_times(path: str, method: str = 'onset') -> typing.List[float]:
    y, sr = librosa.load(path)

    if method == 'beat' or method == 'union':
        _, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beats = {round(time, 3) for time in librosa.frames_to_time(beat_frames, sr=sr)}

    if method == 'onset' or method == 'union':
        onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
        onsets = {round(time, 3) for time in librosa.frames_to_time(onset_frames, sr=sr)}

    if method == 'beat':
        times = list(beats)

    if method == 'onset':
        times = list(onsets)

    if method == 'union':
        times = list(beats.union(onsets))

    times.sort()

    return times

def get_clips(times: list, sources: list, audio: AudioFileClip) -> typing.List[VideoFileClip]:
    counter = 0
    clips: typing.List[VideoFileClip] = []

    # first
    length = times[0]
    clips.extend(sources[(counter) % len(sources)].get_next_slice(length))
    counter += 1

    while counter < (len(times) - 1):
        length = times[counter+1] - times[counter]
        clips.extend(sources[(counter) % len(sources)].get_next_slice(length))
        counter += 1

    # last
    length = audio.duration - times[-1]
    clips.extend(sources[(counter) % len(sources)].get_next_slice(length))

    return clips

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='mvmake',
        description='Snap some clips to music. This script takes an audio file and a directory where video clips are located then tries to match the given clips to the given audio.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        'output',
        type=str,
        help='The name of the output file.'
    )

    parser.add_argument(
        '--music',
        type=str,
        help='Path to the music file.',
        required=True,
        default=argparse.SUPPRESS
    )

    parser.add_argument(
        '--clips',
        type=str,
        help='Path to the directory containing the clips. All the clips will be read from the directory recursively.',
        required=True,
        default=argparse.SUPPRESS
    )

    parser.add_argument(
        '--extensions',
        type=list,
        help='The enabled extensions of the clips. Files with other extensions will not be used.',
        required=False,
        default=EXTENSIONS
    )

    parser.add_argument(
        '--method',
        help='Select to what to snap the clips. Currently there are three methods supported: onset (snap clips to the starting of each note), beat (snap clips to each beat), union (snap clips to both of these)',
        required=False,
        default='onset',
        const='onset',
        nargs='?',
        choices=['onset', 'beat', 'union']
    )

    parser.add_argument(
        '--width',
        type=int,
        help='The width of the output. If given without height, the clips aspect ratio will be kept.',
        required=False,
        default=None
    )

    parser.add_argument(
        '--height',
        type=int,
        help='The height of the output. If given without width, the clips aspect ratio will be kept.',
        required=False,
        default=None
    )

    args = parser.parse_args()

    print(BANNER)

    print('Loading video sources')
    sources = load_source_clips(args.clips, VideoSize(width=args.width, height=args.height), args.extensions)

    print('Loading audio source')
    audio = AudioFileClip(args.music)
    beat_times = get_beat_times(args.music)

    print('Creating frames')
    clips = get_clips(beat_times, sources, audio)

    final = concatenate_videoclips(clips, "compose").set_audio(audio)
    final.write_videofile(args.output)

if __name__ == '__main__':
    main()