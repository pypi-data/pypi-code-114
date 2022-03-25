import _pymeshview
import meshio
import tkinter as tk
import os
import ffmpeg
from tkinter.filedialog import askopenfilename
import argparse


def convert_kwargs_to_args(**kwargs):
    args = type("Arguments", (object,), {"input": None, "output": None, "verbose": False, "no_highlight": False})
    for arg in kwargs:
        try:
            getattr(args, arg)
        except AttributeError:
            print(f"Unknown argument: {arg}")
        setattr(args, arg, kwargs[arg])

    return args


def cleanup_temp_dir(directory):
    for item in os.listdir(directory):
        os.remove(os.path.join(directory, item))

    os.rmdir(directory)


def show_mesh(*normalargs, **kwargs):
    args = normalargs[0] if len(normalargs) > 0 else convert_kwargs_to_args(**kwargs)
    filename = args.input
    if filename is None:
        tk.Tk().withdraw()
        filename = askopenfilename()

    show_window = args.verbose or args.no_highlight
    window = _pymeshview.Window(isVisible=show_window)
    data = meshio.read(filename)
    tet_mesh = _pymeshview.TetMeshBuffer()
    tet_mesh.bufferCells(data.points, data.cells[0].data)
    window.setData(tet_mesh)
    if not os.path.isdir("tmp"):
        os.makedirs("tmp")

    if args.no_highlight:
        window.run()
    else:
        window.highlight(prefixPath="tmp")

    if args.output is not None:
        ffmpeg.input("tmp/output-frame-%01d.png")\
            .filter('fps', fps=30)\
            .output(args.output, pix_fmt='yuv420p').run(overwrite_output=True)

    cleanup_temp_dir("tmp")
