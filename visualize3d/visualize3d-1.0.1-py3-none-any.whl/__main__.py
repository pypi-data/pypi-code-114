import argparse
import open3d
import os
import numpy as np
from .visualize3d import *


def show_files_in_folder(folder: str):
    """
    Show all files in a folder in a loop.
    
    Once a visualization is closed, the next is loaded and shown.
    
    :param folder: The folder over which to iterate.
    """
    files = os.listdir(folder)
    for fname in files:
        if not fname.endswith(".v3d.npy") and not fname.endswith(".pcd"):
            continue
        show_file(os.path.join(folder, fname))


def show_file(filename: str):
    if filename.endswith(".v3d.npy"):
        geometries = load(filename)
    if filename.endswith(".pcd"):
        pcd_o3d = open3d.io.read_point_cloud(filename)
        pcd = np.asarray(pcd_o3d.points)
        geometries = [
            create_pointcloud_from_numpy(pcd),
            create_origin()
        ]
    show(geometries)


def main():
    parser = argparse.ArgumentParser(description='Visualize 3d geometries.')
    parser.add_argument('path', type=str, help='The path to what should be shown.')
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("The path does not exist: {}".format(args.data_path))

    if args.path.endswith(".v3d.npy") or args.path.endswith(".pcd"):
        show_file(args.path)
    else:
        show_files_in_folder(args.path)


if __name__ == "__main__":
    main()
