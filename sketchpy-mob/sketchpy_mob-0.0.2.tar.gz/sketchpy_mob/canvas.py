import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path




class sketch:

    def __init__(self,x_offset = 300, y_offset = 300):
        '''Draw the traced image with help of this sketch function\n
        x-offset - postion of the image in x axis\n
        y-offset - postion of the image in y axis\n
        call the draw_fn() to draw the traced image'''
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset


    def get_coord(self,data):                
        tu = []
        for i in data.readlines():
            i = (i.strip('\n')).strip('(').strip(')')
            tu.append(tuple(map(int,i.split(','))))

        return tu


    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        self.pen.pendown()  


    def paint(self,coord,co=(0,0,0)):
        self.pen.color(co)
        t_x,t_y = coord[0]
        self.go(t_x,t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x,y = i
            if t:
                self.go(x,y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 
        self.pen.end_fill()


    def draw_fn(self,file,mode = 1,co = (0,0,0),thickness = 1,retain = False):

        '''file - path of the file which contains the coordinates\n
        mode - mode of drawing (1 - sketch with line, 0 - fill with color)\n
        co - color of the line or fill\n
        thickness - thickness of the line\n
        retain - retain the image drawn after executing'''

        co = (co[0]/255,co[1]/255,co[2]/255)

        self.pen.color(co)
        data = open(f'{file}.txt','r')
        coord = self.get_coord(data)

        self.pen.width(thickness)
        if mode:
            t_x,t_y = coord[0]
            self.go(t_x,t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x,y = i
                if t:
                    self.go(x,y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        else:
            self.paint(coord=coord,co = co)
        
        if retain:
            tu.done()

    

class ascii_art:
    def __init__(self):
        pass

    def convert_to_acsii(self, img_path, file_name = None) -> str:
        """Converts the given image to ascii art and save it to output_file"""

        from PIL import Image
        # pass the image as command line argument
        img = Image.open(img_path)

        # resize the image
        width, height = img.size
        aspect_ratio = height / width
        new_width = 80
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)

        # convert image to greyscale format
        img = img.convert('L')

        pixels = img.getdata()

        # replace each pixel with a character from array
        chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        # split string of chars into multiple strings of length equal to the new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width]
                    for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)

        # write to a text file.
        if file_name != None:
            with open(f"{file_name}.txt", "w") as f:
                f.write(ascii_image)
        return ascii_image

    def load_data(self,file_path = None, img_path = None, raw_data = None):

        if img_path != None:
            self.data = self.convert_to_acsii(img_path)
        elif file_path != None:
            re = open(file_path, 'r')
            self.data = re.readlines()
        elif raw_data != None:
            self.data = raw_data
            print('sepcify the correct data')
            return
        return self.data

    def draw(self, data):
        #setting the x and y coordinates
        s_x = -320                  
        s_y = 250

        p = tu.Pen()
        p.speed(0)
        tu.bgcolor('black')
        p.up()
        p.width(2)
        f_m = 0
        d_m = 4

        # function to select the color
        def set_col(c):
            chars = {"*": 'white', "S" : 'green', "#" : 'green', "&" : 'white', "@":'black', "$" : 'white', "%" : 'white', "!":'blue', ":" :'darkgreen', ".":'grey'}
            col = chars[c]
            p.pencolor(col)

        def d(m, s_char):
            p.up()
            if s_char != '\n':
                set_col(s_char)

            p.goto(s_x- m, s_y )
            p.down()
            p.forward(1)



        for i in self.data:
            for j in i:
                d(f_m, j)
                f_m -= 4
            s_y -= 9
            s_x = -320
            f_m = 0
            d_m = 4

        tu.done()

    def print_to_terminal(self):
        for i in self.data:
            print(i,end = '')

from tqdm import tqdm
class sketch_from_svg:

    def __init__(self,path,scale=500,x_offset=300,y_offset=300):

        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale

    def hex_to_rgb(self,string):
        strlen = len(string)
        if string.startswith('#'):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1:2]*2
                g = string[2:3]*2
                b = string[3:4]*2
        elif strlen == 3:
                r = string[0:1]*2
                g = string[1:2]*2
                b = string[2:3]*2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]
        
        return int(r,16)/255,int(g,16)/255, int(b,16)/255

    

    def load_svg(self):
        print('loading data')
        paths,attributes,svg_att = svg2paths2(self.path)
        h = svg_att["height"]
        w = svg_att['width']
        self.height = int(h[:h.find('.')])
        self.width = int(w[:w.find('.')])

        res = []
        for i in tqdm(attributes):
            path = parse_path(i['d'])
            co = i['fill']
            #print(co)
            col = self.hex_to_rgb(co)
            #print(col)
            n = len(list(path))+2       
            pts = [((int((p.real/self.width)*self.scale))-self.x_offset, (int((p.imag/self.height)*self.scale))-self.y_offset) for p in (path.point(i/n) for i in range(0,n+1))]
            res.append((pts,col))
            #res.append(pts)
        print('svg data loaded')
        return res

    def move_to(self,x, y):
        self.pen.up()
        self.pen.goto(x,y)
        self.pen.down()


    def draw(self,retain=True):
        coordinates = self.load_svg()
        self.pen = tu.Turtle()
        self.pen.speed(0)
        for path_col in coordinates:
            f = 1
            self.pen.color('black')
            #print(path_col)
            path = path_col[0]
            #print(path_col)
            col = path_col[1]
            #print(col)
            self.pen.color(col)
            self.pen.begin_fill()
            next = 0
            for coord in path:
                #for coord in path_col:
                x,y = coord
                y *= -1
                #print(x,y)
                if f:
                    self.move_to(x, y)
                    f=0
                else:
                    self.pen.goto(x,y)
            self.pen.end_fill()

        if retain == True:
            tu.done()








