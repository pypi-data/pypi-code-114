import numpy as np
import yaml
import cv2

class Parameters:
    """
    Contains all parameters options to perform PIV

    Default values are defined here. There are two options to change the
    values for a specific DPIV run:

    - Change the specific value manually on python shell or on the running
      script.

            Example:  Parameters.box_size_1_x = 128

    - Load all the parameters included in a yaml file by using readPArameters
      classmethod.

            Example: Parameters.readParameters('folder/filename')
    """

    #Default first step parameters
    box_size_1_x = 64   #Cross-correlation box1
    box_size_1_y = 64   #Cross-correlation box1
    no_boxes_1_x = 64   #Number of x-windows
    no_boxes_1_y = 32   #Number of y-windows
    window_x_1 = 48
    window_y_1= 48

    #Default second step parameters
    box_size_2_x = 32   #Cross-correlation box 2
    box_size_2_y = 32   #Cross-correlation box 2
    no_boxes_2_x = 128   #number of x-Windows
    no_boxes_2_y = 64   #Number of y windows
    window_x_2 = 32
    window_y_2 = 32

    #Number of pass of first step
    no_iter_1 = 1
    no_iter_2 = 1

    #default general parameters
    mask = 0
    peak_ratio = 1
    weighting = 0
    gaussian_filter = 0
    median_limit = 0.5
    factor = 1
    dt = 1

    #Extra data needed in some cases
    class Data:
        #path of mask images
        path_mask = "none"

    @classmethod
    def readParameters(self,fileName):
        """
        Read parameters from a yaml file
        """
        with open(fileName) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

            #Default first step parameters
            self.box_size_1_x = data['box_size_1_x']
            self.box_size_1_y = data['box_size_1_y']
            self.no_boxes_1_x = data['no_boxes_1_x']
            self.no_boxes_1_y = data['no_boxes_1_y']
            self.window_x_1 =   data['window_x_1']
            self.window_y_1 =   data['window_y_1']

            #Number of pass of first step
            self.no_iter_1 = data['no_iter_1']
            self.no_iter_2 = data['no_iter_2']

            #Default first step parameters
            self.box_size_2_x = data['box_size_2_x']
            self.box_size_2_y = data['box_size_2_y']
            self.no_boxes_2_x = data['no_boxes_2_x']
            self.no_boxes_2_y = data['no_boxes_2_y']
            self.window_x_2 =   data['window_x_2']
            self.window_y_2 =   data['window_y_2']

            #default general parameters
            self.mask = data['mask']
            self.peak_ratio = data['peak_ratio']
            self.weighting = data['weighting']
            self.gaussian_filter = data['gaussian_filter']
            self.median_limit = data['median_limit']
            self.factor = data['factor']
            self.dt = data['dt']

            #Extra data
            if self.mask:
                if data['path_mask'].endswith('.np'):
                    self.Data.mask = bool(np.load(data['path_mask']))
                else:
                    self.Data.mask = np.asarray(cv2.cvtColor(cv2.imread(
                        data['path_mask']), cv2.COLOR_BGR2GRAY)).astype(bool)

    def introParameters():
        """
        Introduce a parameter manually, not implemented yet (probably
        needed for a GUI)
        """
        pass

class grid:

    @classmethod
    def generate_mesh(cls,width,height):

        """
        Generates the meshgrid of x and y position for the correlation
        windows in the two passes, according to the piv parameters selected.
        """
        pixels = width*height


        #Obtain PIV Mesh for calculationsFp_Top + Fp_Down
        box_origin_x_1 = (1+np.round((np.arange(0,Parameters.no_boxes_1_x)
            *(width-Parameters.box_size_1_x-2))
            /(Parameters.no_boxes_1_x-1)).astype(np.int32))
        box_origin_y_1 = (1+np.round((np.arange(0,Parameters.no_boxes_1_y)
            *(height-Parameters.box_size_1_y-2))
            /(Parameters.no_boxes_1_y-1)).astype(np.int32))

        x_1 = (box_origin_x_1-1+Parameters.box_size_1_x/2).astype(np.int32)
        y_1 = (box_origin_y_1-1+Parameters.box_size_1_y/2).astype(np.int32)

        [x_1, y_1] = np.meshgrid(x_1,y_1)
        [box_origin_x_1, box_origin_y_1] = np.meshgrid(
                box_origin_x_1, box_origin_y_1)

        x_margin = 3/2 * np.amax(
                [Parameters.box_size_1_x, Parameters.box_size_2_x])
        y_margin = 3/2 * np.amax(
                [Parameters.box_size_1_y, Parameters.box_size_2_y])

        #second grid is placed completely inside first one
        x_2 = np.int32(2 + np.round(np.arange(0, Parameters.no_boxes_2_x) *
            (width-x_margin-6)/(Parameters.no_boxes_2_x-1)+x_margin/2))
        y_2 = np.int32(2 + np.round(np.arange(0, Parameters.no_boxes_2_y) *
            (height-y_margin-6)/(Parameters.no_boxes_2_y-1)+y_margin/2))

        [x_2, y_2] = np.meshgrid(x_2, y_2)

        box_origin_x_2 = (x_2-Parameters.box_size_2_x/2).astype(np.int32)
        box_origin_y_2 = (y_2-Parameters.box_size_2_y/2).astype(np.int32)

        cls.x_1 = x_1.astype(np.int32)
        cls.y_1 = y_1.astype(np.int32)
        cls.x_2 = x_2.astype(np.int32)
        cls.y_2 = y_2.astype(np.int32)
        cls.box_origin_x_1 = box_origin_x_1.astype(np.int32)
        cls.box_origin_y_1 = box_origin_y_1.astype(np.int32)
        cls.box_origin_x_2 = box_origin_x_2.astype(np.int32)
        cls.box_origin_y_2 = box_origin_y_2.astype(np.int32)

    def read_mesh(self,height,width):
        """
        Read the positions of a custon mesh from a file (not implemented yet)
        """
        pass

class Synt_Img():
    """
    Contains parameters of to generate a pair of sintetic images following
    a certain flow velocity field. The default values can be changed manually.

    Variables:
    ----------
    Width: int
        Number of pixels on the x-direction of the generated image.

    height: int
        Number of pixels on the y-direction of the generated image.

    trazers_density: float
        Number of particles generated per pixel. Needs to be some float
        between 0 and 1

    vel: float
        Caracteristic velocity of the canonical flow used for generate the
        particles displacement.

        Note: It has a diferent definition on each flow.

    Shine_m: int
        Mean shine of the trazers core (from 0 to 255).

    d_Shine: int
        Triangular variability of the trazers shine.

    D_m: int or float
        Mean diameter of the trazers.

    d_D: int or float
        triangular variability of the trazers diameter.

    noise_m: int
        mean of the random noise.

    d_noise: int
        triangular variability of the random noise.

    vel_profile: str
        Name of the flow velocity field used. The following options are
        avaiable:

            Constant: Flow with a constant displacement of "vel" pixels on
                      the x-direction

            Couette: Couette flwo in x-direction using a moving condition
                     of "vel" pixels between images on top wall. Bottom
                     limit of the images is not moving.

            Poiseuille: Poiseuille flow in x direction with no-slip condition
                        on top and bottom of the images. The parameter "vel"
                        indicates de maximun velicity of the flow in pixels.

            Vortex: Flow generated by a Scully vortex (see Scully 1975). Vel
                    is the maximun velocity of the vortex in pixel/frame.

            Frequency: Spatial frequency wave along y-direction. This flow
                       allows to test the PIV frequency response (see akfda
                       1992). In this case, the maximun pixel displacement
                       on the wave is always 2 pixels, and the parameter
                       "vel" indicates the wavelength.

    ext: str
        Extension of the images to be saved

    """

    width = 1024               #Width of generated image
    height = 1024              #height of generated image
    vel_profile = 'Vortex'     #(Constant, Couette, Poiseuille, Rankine)
    vel = 8                    #Velocity in pixels/fotogram
    trazers_density = 0.05     #Number of trazers/ pixel
    Shine_m = 230              #Mean shine of trazers
    d_Shine = 80               #Variability for randon shine of trazers
    D_m = 6                    #Mean diameter of trazers (in pixels)
    d_D = 3                    #Variability for random diameter of trazers
    noise_m = 1                #Mean white noise of the image
    d_noise = 1                #Variability of the noise of the image
    ext = '.png'               #Image save format

class GPU():

    def gpu_data(self,thr):
        pass
