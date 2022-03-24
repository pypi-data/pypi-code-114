from EChart import EChart
from utils import princess
import time
import os


class LineChart(EChart):

    def __init__(self, global_args, options):
       super(LineChart, self).__init__(global_args)
       self.options = options

    def get_options(self):
        return self.options

    def set_options(self, attrs, values):
       for attr, value in attrs, values:
           attr = attr.split(".")
    
    def output(self,type, o_path="log/" + time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()) ):
        if type == "html":
            if not os.path.exists("log"):
                os.makedirs("log")
            os.makedirs(o_path+"/html/js/")
            fd = os.open(o_path+"/html/main.html",os.O_RDWR|os.O_CREAT)
            os.write(fd, str(princess.echart2html(self)).encode())
            os.close(fd)
            fd = os.open(o_path+"/html/js/charts_cfg.js",os.O_RDWR|os.O_CREAT|os.O_APPEND)
            os.write(fd, princess.js_init_echart(self).encode())
            os.write(fd, princess.js_init_chartOption(self).encode())
            os.close(fd)
            
