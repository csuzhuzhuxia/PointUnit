from laspy.file import File
import numpy as np
import open3d

def get_point(filename,verbose=False):
    """
    input:
        filename: str
        verbose: whether print(now for las file)
    output:
        points:numpy array (shape:[num_point,3])
    """
    postfix = filename.split(".")[-1]
    if(postfix=="pcd"):
        points = np.asarray(open3d.io.read_point_cloud(filename).points)
    elif(postfix=="las"):
        inFile = File(filename, mode='r')
        if verbose:
            print(vars(inFile))
        points = np.asarray([inFile.x,inFile.y,inFile.z]).reshape([-1,3])
    elif(postfix=="txt"):
        points = np.loadtxt(filename)
    elif(postfix=="npy"):
        points = np.load(filename)
    return points