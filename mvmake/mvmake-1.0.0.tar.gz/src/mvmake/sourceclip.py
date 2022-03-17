import typing

from moviepy.editor import VideoFileClip

from .videosize import VideoSize

class SourceClip():
    def __init__(self, path: str, target_resolution: VideoSize = (None, None)):
        self.clip = VideoFileClip(path, False, False, 200000, target_resolution=(target_resolution.height, target_resolution.width))
        self.time = 0

    def get_next_slice(self, length: float) -> typing.List[VideoFileClip]:
        start = self.time
        self.time = start + length

        if self.time > self.clip.duration:
            # TODO: this could fail if length is longer than clip's duration (test with very short clips)
            self.time = (start + length) % self.clip.duration

            return [
                self.clip.subclip(start),
                self.clip.subclip(0, self.time)
            ]

        return [self.clip.subclip(start, self.time)]