import os


def fileparts(fullpath):
    residual, ext = os.path.splitext(path)
    path, file = os.path.split(residual)
    
    return path,file, ext
