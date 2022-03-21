import glob
from PIL import Image


class GIFDescriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        print(f"__get__ has been called. {value}")
        return value

    def __set__(self, obj, value):
        for i in value:
            if i <= 0:
                raise ValueError("Size tuple values must be bigger than 0")

        print(f"__set__ has been called. {value}")
        setattr(obj, self.private_name, value)


class GIFManager:
    """
        path_in : Path of original images(Ex: ./images/*.png), default is None
        path_out : Path you want to place result image(Ex: ./output/) Don't forget to put last slash(/), default is None
        file_name : Name of result image, default is None
        size : Must be tuple, If you want to resize, give this argument. default is (320, 320).
        duration: Duration of result image. default is 1000(ms)
    """

    size = GIFDescriptor()

    def __init__(
        self,
        path_in=None,
        path_out=None,
        file_name=None,
        size=(320, 320),
        duration=1000,
    ):

        self.path_in = path_in or "./*.png"
        self.path_out = path_out or "./"
        self.file_name = file_name or "result"
        self.size = size
        self.duration = duration

    def make_gif(self):
        """
        Execute making GIF
        """
        img, *images = [
            Image.open(f).resize(self.size, Image.ANTIALIAS)
            for f in sorted(glob.glob(self.path_in))
        ]

        outpath_onsave = f"{self.path_out}{self.file_name}.gif"

        try:
            img.save(
                fp=outpath_onsave,
                format="GIF",
                append_images=images,
                save_all=True,
                duration=self.duration,
                loop=0,
            )
        except IOError:
            print("Cannot convert! : ", img)
