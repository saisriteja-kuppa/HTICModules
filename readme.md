# HTIC Modules

## Bounding Box Module
This consists of function to create a set of points in a bounding box

```python
from boundingboxmodules.boundingbox import getboxpoints, plotpoints
points = getboxpoints(DiagonalP1, DiagonalP2, [x_thresh, y_thresh, z_thresh])
plotpoints(points, status_list, filter= None)
```
