import geopandas as gp
from shapely.geometry import Point


class Readboundry():
    def __init__(self, path):
        self.path = path

        self.Boundryfile = gp.read_file(self.path)
        self.code_dict = {
            i: self.Boundryfile[self.Boundryfile['district_c'] == i]
            ['geometry'].tolist()[0]
            for i in self.Boundryfile['district_c'].tolist()
        }

    def within(self, lat, lng, code):
        if code not in self.code_dict:
            return '边界文件中不含该乡'
        p1 = Point(float(lng), float(lat))
        return p1.within(self.code_dict[code])
