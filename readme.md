# HTIC Modules

## Bounding Box Module
This consists of function to create a set of points in a bounding box

```python
from boundingboxmodules.boundingbox import getboxpoints, plotpoints
points = getboxpoints(DiagonalP1, DiagonalP2, [x_thresh, y_thresh, z_thresh])
plotpoints(points, status_list, filter= None)
```



## Lotus Module
This contains the lotus module to 12 different entry points at  regular intervals of 30 in angulation for the same target point.


```python
import numpy as np
from lotus import getSphericalCoords
entry= np.array([-370 ,  400, 60.0])
needle_length = 145
elevation_angle = 45
target = entry - np.array([0,0,needle_length])
entry = np.array(entry)
entries = getSphericalCoords(target, needle_length, elevation_angle)[:,0]
```

