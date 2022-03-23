from svgutils.compose import *
import numpy as np
from IPython.display import display
from importlib import resources

def get_resource(module: str, name: str) -> str:
    return resources.files(module).joinpath(name)

class Segment(object):
    def __init__(self, s: str):
        s = s.lower()
        self.__figure__ = None
        if (s == 'aa'):
            self.info = {
                'length': 660,
                'type': '8F1I01.AA66.xxxx-1',
                'description': 'ACOPOStrak straight segment'
            }
            self.__svg__ = 'segment_aa.svg'
            self.__img__ = {'tl': (0.0, 0.25),
                            'bl': (0.0, 10.74),
                            'tr': (66.0, 0.25),
                            'br': (66.0, 10.74),
                            'w': 66.0,
                            'h': 10.074,
                            'rs': 0.0,
                            're': 0.0}
        elif (s == 'ab'):
            self.info = {
                'length': 450,
                'type': '8F1I01.AB2B.xxxx-1',
                'description': 'ACOPOStrak curve segment A'
            }
            self.__svg__ = 'segment_ab.svg'
            self.__img__ = {'tl': (0.0, 0.25),
                            'bl': (0.0, 9.98),
                            'tr': (44.6, 3.56),
                            'br': (40.89, 12.523),
                            'w': 44.6,
                            'h': 12.523,
                            'rs': 0.0,
                            're': 22.5}
        elif (s == 'ba'):
            self.info = {
                'length': 450,
                'type': '8F1I01.BA2B.xxxx-1',
                'description': 'ACOPOStrak curve segment B'
            }
            self.__svg__ = 'segment_ba.svg'
            self.__img__ = {'tl': (0.0, 3.56),
                            'bl': (3.71, 12.523),
                            'tr': (44.6, 0.25),
                            'br': (44.6, 9.98),
                            'w': 44.6,
                            'h': 12.523,
                            'rs': 22.5,
                            're': 0.0}
        elif (s == 'bb'):
            self.info = {
                'length': 240,
                'type': '8F1I01.BB4B.xxxx-1',
                'description': 'ACOPOStrak circular arc segment'
            }
            self.__svg__ = 'segment_bb.svg'
            self.__img__ = {'tl': (0.0, 2.59),
                            'bl': (4.35, 13.081),
                            'tr': (23.2, 2.59),
                            'br': (18.85, 13.081),
                            'w': 23.2,
                            'h': 13.081,
                            'rs': 22.5,
                            're': 22.5}
        else:
            raise ValueError('Segment not supported')
    
    def plot(self, angle = 0):
        angle %= 360.0
        w = self.__img__['w']
        h = self.__img__['h']
        
        nw = (abs(w*np.cos(np.deg2rad(angle))) + abs(h*np.cos(np.deg2rad(90+angle)))).round(3)
        nh = (abs(w*np.sin(np.deg2rad(angle))) + abs(h*np.sin(np.deg2rad(90+angle)))).round(3)
        nx = (nw - ((w*np.cos(np.deg2rad(angle))) + (h*np.cos(np.deg2rad(90+angle)))).round(3))/2
        ny = (nh - ((w*np.sin(np.deg2rad(angle))) + (h*np.sin(np.deg2rad(90+angle)))).round(3))/2
        
        self.__figure__ = Figure(str(nw) + 'mm', str(nh) + 'mm', SVG(get_resource('img', self.__svg__)).move(nx,ny).rotate(angle))
        
        display(self.__figure__)
        
        return self
    
    def save(self, name = ''):
        if name == '':
            self.__figure__.save('segment.svg')
        else:
            self.__figure__.save(name)
            
    def __add__(self, other):
        if (isinstance(other, Segment)):
            new_track = Track([self, other])
            return new_track
        elif(isinstance(other, Track)):
            new_track = other.segments.copy()
            new_track.append(self)
            return Track(new_track)
    
    def __mul__(self, other):
        if(isinstance(other, int)):
            new_track = Track([self])
            r_track = new_track.segments * other
            return Track(r_track)
    
    __rmul__ = __mul__
    
class Track(object):
    def __init__(self, segments):
        self.segments = list(segments)
        
    def __add__(self, other):
        new_track = self.segments.copy()
        if (isinstance(other, Segment)):
            new_track.append(other)
        elif(isinstance(other, Track)):
            new_track = new_track + other.segments
        return Track(new_track)
    
    def __mul__(self, other):
        if(isinstance(other, int)):
            new_track = self.segments.copy()
            new_track = new_track * other
            return Track(new_track)
    
    def __len__(self):
        return len(self.segments)
    
    def length(self):
        return sum(s.info['length'] for s in self.segments)
    
    def plot(self, angle = 0):
        angle %= 360.0
        xabs = self.segments[0].__img__['tl'][0]
        yabs = self.segments[0].__img__['tl'][1]
        rot = angle
        gap = 0.5
        xmax = 0.0
        ymax = 0.0
        xmin = 0.0
        ymin = 0.0

        asm = []
        for seg in self.segments:
            rot += seg.__img__['rs']
            xabs += (seg.__img__['tl'][1] * np.sin(np.deg2rad(rot)))
            yabs -= (seg.__img__['tl'][1] * np.cos(np.deg2rad(rot)))
            
            w = seg.__img__['w']
            h = seg.__img__['h']
            nw = [(w*np.cos(np.deg2rad(rot))).round(3), (h*np.cos(np.deg2rad(90+rot))).round(3)]
            nh = [(w*np.sin(np.deg2rad(rot))).round(3), (h*np.sin(np.deg2rad(90+rot))).round(3)]
            
            xmax = max(xmax, xabs, xabs + sum(x for x in nw if x > 0))
            ymax = max(ymax, yabs, yabs + sum(y for y in nh if y > 0))
            xmin = min(xmin, xabs, xabs + sum(x for x in nw if x < 0))
            ymin = min(ymin, yabs, yabs + sum(y for y in nh if y < 0))
    
            asm.append(SVG(get_resource('img', seg.__svg__)).move(round(xabs, 3), round(yabs, 3)).rotate(round(rot, 3)))
    
            xabs += ((seg.__img__['tr'][0] * np.cos(np.deg2rad(rot))) + (seg.__img__['tr'][1] * np.cos(np.deg2rad(rot + 90))) + (gap * np.cos(np.deg2rad(rot))))
            yabs += ((seg.__img__['tr'][0] * np.sin(np.deg2rad(rot))) + (seg.__img__['tr'][1] * np.sin(np.deg2rad(rot + 90))) + (gap * np.sin(np.deg2rad(rot))))
            rot +=  seg.__img__['re']
        
        nw = (abs(xmax) + abs(xmin))
        nh = (abs(ymax) + abs(ymin))
        nx = abs(xmin)
        ny = abs(ymin)
        
        self.__figure__ = Figure(str(nw) + 'mm', str(nh) + 'mm', *asm).move(nx, ny)
        display(self.__figure__)
        
        return self
    
    def save(self, name = ''):
        if name == '':
            self.__figure__.save('track.svg')
        else:
            self.__figure__.save(name)
    
    __rmul__ = __mul__
    
class Loop(Track):
    def __init__(self, l = 2, w = 1):
        self.length = l
        self.width = w
        if (self.length < 2):
            raise ValueError('The length of the loop must be at least 2')
        elif (self.width < 1):
            raise ValueError('The width of the loop must be at least 1')
        else:
            if (self.width == 1):
                self._track = TRACK180 + ((self.length - 2) * TRACK0) + TRACK180 + ((self.length - 2) * TRACK0)
            else:
                self._track = TRACK90 + ((self.width - 2) * TRACK0) + TRACK90 + ((self.length - 2) * TRACK0) + TRACK90 + ((self.width - 2) * TRACK0) + TRACK90 + ((self.length - 2) * TRACK0)
        super().__init__(self._track.segments)

TRACK0 = Track([Segment('aa')])
TRACK45 = Track([Segment('ab'), Segment('ba')])
TRACK90 = Track([Segment('ab'), Segment('bb'), Segment('ba')])
TRACK135 = Track([Segment('ab'), Segment('bb'), Segment('bb'), Segment('ba')])
TRACK180 = Track([Segment('ab'), Segment('bb'), Segment('bb'), Segment('bb'), Segment('ba')])