import math
import numpy as np 
from .get_image_size import get_image_size
from PIL import Image
import os
import shutil
        
class CVSlicer:
    def __init__(self, img_path, height_cutoff, width_cutoff, object_height, object_width):
        self.temp_folder_name = "__temp_cvslicer"
        
        if os.path.exists(self.temp_folder_name):
            shutil.rmtree(self.temp_folder_name)
        os.makedirs(self.temp_folder_name)
        
        self.load_image(img_path)
        self.number_of_image_saved = 0
        
        self.height_cutoff = height_cutoff
        self.width_cutoff = width_cutoff
        self.cutoff_point_height = []
        self.cutoff_point_width = []
        
        # Enlarge the object size by 10 % extra just for safety sake
        self.object_height = int(1.1*object_height)
        self.object_width = int(1.1*object_width)
        
        self.validate_parameter()
        
        # To grab how many pieces we can get sliced the image horizontally and vertically 
        self.number_cutoff_height = int(math.ceil(self.img_height/self.height_cutoff))
        self.number_cutoff_width = int(math.ceil(self.img_width/self.width_cutoff))

        return
    
    def load_image(self, img_path):
        self.img_width, self.img_height = get_image_size(img_path)
        Image.MAX_IMAGE_PIXELS = int(self.img_width*self.img_height)
        image = Image.open(img_path)
        self.img_ori = image
        
        return
    
    def convert_to_cv_img(self, img_pil):
        image = img_pil.convert('RGB') 
        image = np.array(image) 
        # Convert RGB to BGR 
        image = image[:, :, ::-1].copy()
        return image
    
    def throw_memory_to_hardisk(self, img_pil):
        file_path = self.temp_folder_name+"\\"+str(self.number_of_image_saved)+".png"
        img_pil = img_pil.save(file_path)
        self.number_of_image_saved += 1    
        return file_path
        
    def validate_parameter(self):
        if 2*self.object_height >= self.height_cutoff:
            self.img_ori.close()
            raise Exception("Object's height cannot be equal or taller than 0.5 of cutoff height.")
        if 2*self.object_width >= self.width_cutoff:
            self.img_ori.close()
            raise Exception("Object's width cannot be equal or wider than 0.5 of cutoff width.")    
        return
        
    def slice_img(self):
        output_images = []
        output_images += self.slice_img_by_borders();
        output_images += self.slice_img_around_vertical_borders();
        output_images += self.slice_img_around_horizontal_borders();
        output_images += self.slice_img_around_intersection_of_borders();
        self.img_ori.close()
        return output_images
    
    def slice_img_by_borders(self):
        output_images = []
        for i in range(1, self.number_cutoff_width+1):
            for j in range(1, self.number_cutoff_height+1):
                height_start = (j-1)*self.height_cutoff
                height_end = min( self.img_height, j*self.height_cutoff)
                
                width_start = (i-1)*self.width_cutoff
                width_end = min( self.img_width, i*self.width_cutoff)
                
                if height_end != self.img_height and height_end not in self.cutoff_point_height:
                    self.cutoff_point_height.append(height_end)
                    
                if width_end != self.img_width and width_end not in self.cutoff_point_width:
                    self.cutoff_point_width.append(width_end)
                
                cropped_image = self.img_ori.crop((width_start, height_start, width_end, height_end))
                output_img_path = self.throw_memory_to_hardisk(cropped_image)
                output_images.append([output_img_path, [width_start, height_start]])
        return output_images

    def slice_img_around_horizontal_borders(self):
        output_images = []
        for j in range(1, self.number_cutoff_height+1):
            for each_cutoff_point_width in self.cutoff_point_width:
                height_start = (j-1)*self.height_cutoff
                height_end = min( self.img_height, j*self.height_cutoff)
                
                width_start = each_cutoff_point_width - self.object_width
                width_end = each_cutoff_point_width + self.object_width
                cropped_image = self.img_ori.crop((width_start, height_start, width_end, height_end))
                output_img_path = self.throw_memory_to_hardisk(cropped_image)
                output_images.append([output_img_path, [width_start, height_start]])
        return output_images
            
    def slice_img_around_vertical_borders(self):
        output_images = []
        for i in range(1, self.number_cutoff_width+1):
            for each_cutoff_point_height in self.cutoff_point_height:
                height_start = each_cutoff_point_height - self.object_height
                height_end = each_cutoff_point_height + self.object_height
                
                width_start = (i-1)*self.width_cutoff
                width_end = min( self.img_width, i*self.width_cutoff)
                cropped_image = self.img_ori.crop((width_start, height_start, width_end, height_end))
                output_img_path = self.throw_memory_to_hardisk(cropped_image)
                output_images.append([output_img_path, [width_start, height_start]])
        return output_images
    
    def slice_img_around_intersection_of_borders(self):
        output_images = []
        for each_cutoff_point_width in self.cutoff_point_width: 
            for each_cutoff_point_height in self.cutoff_point_height:
                height_start = each_cutoff_point_height - self.object_height
                height_end = min( self.img_height, each_cutoff_point_height + self.object_height)
                
                width_start = each_cutoff_point_width - self.object_width
                width_end = min( self.img_width, each_cutoff_point_width + self.object_width)
                cropped_image = self.img_ori.crop((width_start, height_start, width_end, height_end))
                output_img_path = self.throw_memory_to_hardisk(cropped_image)
                output_images.append([output_img_path, [width_start, height_start]])
        return output_images
        
