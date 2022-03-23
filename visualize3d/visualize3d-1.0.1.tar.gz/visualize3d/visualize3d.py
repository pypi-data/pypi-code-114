from typing import Optional
import open3d
import numpy as np


def create_pointcloud_from_numpy(pointcloud: np.ndarray, colors: Optional[np.ndarray] = None):
    """
    Create a pointcloud given a numpy array.
    
    :param pointcloud: A numpy array of shape (N, 3) representing the pointcloud.
    :param colors: (Optional) A numpy array of the same shape as the pointcloud representing the colors for the points.
    :return: A geometry object.
    """
    return {"pcl": {"pcl": pointcloud, "colors": colors}}


def create_lines_from_numpy(points: np.ndarray, lines: np.ndarray, colors: Optional[np.ndarray] = None):
    """
    Create lines from numpy arrays.
    
    :param points: A numpy array of shape (N, 3) representing the points in 3d space that should be connected.
    :param lines: A numpy array of shape (N, 2) where the values are the indices of the points that should be connected.
    :param colors: (Optional) A numpy array of the same shape as the lines representing the colors for the lines.
    :return: A geometry object.
    """
    return {"lines": {"points": points, "lines": lines, "colors": colors}}


def create_origin(origin=[0, 0, 0], size=1.5):
    """
    Create an origin in the visualization at the given position.
    
    :param origin: The 3d position of the origin. (default: `[0,0,0]`)
    :param size: The size of the origin. (default: `1.5`)
    :return: A geometry object.
    """
    return {"origin": {"origin": origin, "size": size}}


def show(geometries):
    """
    Renders the geometries given in an interactive window.
    
    You can use the mouse to navigate the view. See the documentation of open3d for more details on navigation in the viewer.
    
    :param geometries: A list of geometry objects that should be plotted.
    """
    o3d_geometries = []
    for geometry in geometries:
        if "pcl" in geometry:
            point_cloud = open3d.geometry.PointCloud()
            point_cloud.points = open3d.utility.Vector3dVector(geometry["pcl"]["pcl"])
            colors = geometry["pcl"]["colors"]
            if colors is None:
                colors = np.zeros_like(geometry["pcl"]["pcl"])
            point_cloud.colors = open3d.utility.Vector3dVector(colors)
            o3d_geometries.append(point_cloud)
        elif "lines" in geometry:
            line_set = open3d.geometry.LineSet()
            line_set.points = open3d.utility.Vector3dVector(geometry["lines"]["points"])
            line_set.lines = open3d.utility.Vector2iVector(geometry["lines"]["lines"])
            colors = geometry["lines"]["colors"]
            if colors is None:
                colors = np.zeros_like(geometry["lines"]["points"])
            line_set.colors = open3d.utility.Vector3dVector(colors)
            o3d_geometries.append(line_set)
        elif "origin" in geometry:
            o3d_geometries.append(open3d.geometry.TriangleMesh.create_coordinate_frame(size=geometry["origin"]["size"], origin=geometry["origin"]["origin"]))
    open3d.visualization.draw_geometries(o3d_geometries)


def save(output_file: str, geometries):
    """
    Save the geometries given to the disk.
    
    :param output_file: The file where to store the geometries. (Should be `*.npy`-file)
    :param geometries: A list of geometry objects that should be stored.
    """
    np.save(output_file, geometries)


def load(input_file: str):
    """
    Load geometries from the disk.
    
    :param input_file: The file where to load the geometries. (Should be `*.npy`-file)
    :return: A list of geometry objects that are stored in the file.
    """
    return np.load(input_file, allow_pickle=True)
