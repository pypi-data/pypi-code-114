
import os
import requests
import re
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtGui

def relative_path(path):
    this_dir = os.path.dirname(__file__)
    return os.path.join(this_dir, path)

def markdown_to_label(markdown_text, label):
    label.setText(markdown_text)
    label.setWordWrap(True)

class FeedUpdater(QObject):
    finished = pyqtSignal(list)

    def set_feed(self, feed):
        self.feed = feed

    def run(self):
        items = []
        for i in range(20):
            try:
                next_item = next(self.feed)
            except StopIteration:
                break
            except KeyError:
                continue
            except ConnectionError:
                window.connecting_screen()
                break
            if next_item:
                items.append(next_item)
        self.finished.emit(items)

IMAGE_DIR = relative_path('./images/')

thumb_path = '/tmp/lyberry_thumbs/'
if not os.path.isdir(thumb_path):
    os.mkdir(thumb_path)

def download_file(url):
    local_filename = thumb_path+str(hash(url))
    if os.path.isfile(local_filename):
        return local_filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename


class ImageLoader(QObject):
    finished = pyqtSignal(QtGui.QPixmap)

    def set_url(self, url):
        self.url = url

    def run(self):
        pixmap = QtGui.QPixmap()
        try:
            file = download_file(self.url)
            pixmap.load(file)
            del file
            self.finished.emit(pixmap)
            return
        except Exception as err:
            print(f'Error loading image: {err}')
            self.default()
    
    def default(self):
        pixmap = QtGui.QPixmap()
        pixmap.load(IMAGE_DIR+'NotFound.png')
        self.finished.emit(pixmap)

def make_chapter_file(pub):
    with open('/tmp/lyberry_chapters', 'w') as chapters_file:
        chapters_file.write(desc_to_ffmetadata(pub.description))

def desc_to_ffmetadata(desc: str, end: int = 0) -> str:
    lines = desc.split('\n')
    matches = []
    for line in lines:
        match = re.match(r'\s*(\d+:\d+)\s(.*)', line)
        if match:
            matches.append(match)

    stamps = []
    for match in matches:
        raw_time = match.group(1)
        [minutes, seconds] = raw_time.split(':')
        time = int(minutes)*60 + int(seconds)
        title = match.group(2)
        stamps.append([time, title])

    out = ';FFMETADATA1'
    for i, stamp in enumerate(stamps):
        time = stamp[0]
        title = stamp[1]
        out += f'''
[CHAPTER]
TIMEBASE=1/1
START={time}
'''
        if i+1 < len(stamps):
            next_time = stamps[i+1][0]
            out += f'END={next_time}\n'
        elif end != 0:
            out += f'END={end}\n'
        else:
            out += f'END={next_time + 100}\n'
        out += f'title={title}\n'
    return out

