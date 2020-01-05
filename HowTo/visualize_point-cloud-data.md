# Table of Contents <a href=table-of-contents-></a>

- [Visualizing Point Cloud Data](#visualizing-point-cloud-data-)
  * [Python Library: `open3d`](#python-open3d-docs)
  * [Working with Numpy: Example](#open3d-working-with-numpy-example)
    + [From NumPy to `open3d.PointCloud`](#from-numpy-to-open3dpointcloud-)
    + [From open3d.PointCloud to NumPy](#from-open3dpointcloud-to-numpy-)
  * [Jupyter Visualization](#jupyter-viz)
  * [Stackoverflow](#stackoverflow)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

---

# Visualizing Point Cloud Data <a href=visualizing-point-cloud-data-></a>
Point cloud data is used or generated in a lot of emerging fields, such as LIDARS used for autonomous cars. 
And visualization and manipulation of pointcloud data is a very important requirement for people involved with 
research in such fields.

_Disclaimer_: Some or most of the code here is just put-together from various sources as mentioned below 
using hyperlinks whenever applicable.


[TOC](#table-of-contents-)

---
## Python Library: [`open3d`](http://www.open3d.org/docs) <a name="python-open3d-docs"></a>
## [Working with Numpy: Example](http://www.open3d.org/docs/release/tutorial/Basic/working_with_numpy.html)  <a name="open3d-working-with-numpy-example"></a>
This shows how to save/load a numpy [x,y,z] array of points as a `.ply` (polygon) file.  

```python
# examples/Python/Basic/working_with_numpy.py

import copy
import numpy as np
import open3d as o3d

if __name__ == "__main__":

    # generate some neat n times 3 matrix using a variant of sync function
    x = np.linspace(-3, 3, 401)
    mesh_x, mesh_y = np.meshgrid(x, x)
    z = np.sinc((np.power(mesh_x, 2) + np.power(mesh_y, 2)))
    z_norm = (z - z.min()) / (z.max() - z.min())
    xyz = np.zeros((np.size(mesh_x), 3))
    xyz[:, 0] = np.reshape(mesh_x, -1)
    xyz[:, 1] = np.reshape(mesh_y, -1)
    xyz[:, 2] = np.reshape(z_norm, -1)
    print('xyz')
    print(xyz)

    # Pass xyz to Open3D.o3d.geometry.PointCloud and visualize
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_point_cloud("../../TestData/sync.ply", pcd)

    # Load saved point cloud and visualize it
    pcd_load = o3d.io.read_point_cloud("../../TestData/sync.ply")
    o3d.visualization.draw_geometries([pcd_load])

    # convert Open3D.o3d.geometry.PointCloud to numpy array
    xyz_load = np.asarray(pcd_load.points)
    print('xyz_load')
    print(xyz_load)

    # save z_norm as an image (change [0,1] range to [0,255] range with uint8 type)
    img = o3d.geometry.Image((z_norm * 255).astype(np.uint8))
    o3d.io.write_image("../../TestData/sync.png", img)
    o3d.visualization.draw_geometries([img])
```
[TOC](#table-of-contents-)

### From NumPy to `open3d.PointCloud` <a href=from-numpy-to--open3dpointcloud-></a>
```python
    # Pass xyz to Open3D.o3d.geometry.PointCloud and visualize
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    o3d.io.write_point_cloud("../../TestData/sync.ply", pcd)
```

### From open3d.PointCloud to NumPy <a href=from-open3dpointcloud-to-numpy-></a>
```python
    # Load saved point cloud and visualize it
    pcd_load = o3d.io.read_point_cloud("../../TestData/sync.ply")
    o3d.visualization.draw_geometries([pcd_load])

    # convert Open3D.o3d.geometry.PointCloud to numpy array
    xyz_load = np.asarray(pcd_load.points)
    print('xyz_load')
    print(xyz_load)
```
[TOC](#table-of-contents-)

## [Jupyter Visualization](http://www.open3d.org/docs/release/tutorial/Basic/jupyter.html#jupyter-visualization) <a name="jupyter-viz"></a>
[Source](http://www.open3d.org/docs/release/tutorial/Basic/jupyter.html#jupyter-visualization)
>Since version 0.4.0, we added experimental support for Jupyter visualization with WebGL. 
If Open3D is installed from pip or conda repository, Jupyter supported is enabled by default.

```python
import numpy as np
import open3d as o3
from open3d import JVisualizer

pts_path = "examples/TestData/fragment.ply"
fragment = o3.read_point_cloud(pts_path)
visualizer = JVisualizer()
visualizer.add_geometry(fragment)
visualizer.show()
```

[TOC](#table-of-contents-)

---
## Stackoverflow 
1. Stackoverflow Question: [Python - Display 3D Point Cloud [closed]](https://stackoverflow.com/questions/50965673/python-display-3d-point-cloud)
**Install open3d.**
```
pip install open3d
```

**Run the following code.**
```python
import numpy as np
from open3d import *    

def main():
    pcd = read_point_cloud("test.ply") # Read the point cloud
    draw_geometries([pcd]) # Visualize the point cloud     

if __name__ == "__main__":
    main()
```

[TOC](#table-of-contents-)

---
>Last Updated: 2020-Jan-05
