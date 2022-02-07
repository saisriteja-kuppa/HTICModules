import numpy as np
import math





def AnglebtwnVecs(vec1,vec2): 
    """ Angle between two vectors.

    Args:
        vec1 (list): Vector 1 (3*1)
        vec2 (list): Vector 2 (3*1)

    Returns:
        [type]: [description]
    """
              
    angle = np.arccos(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    # print("Angle : {}".format((angle*180)/math.pi))
    return angle

def sphericalRelative(t1_rad, t2_rad, targetP, r):    
    """[summary]

    Args:
        t1_rad ([type]): [description]
        t2_rad ([type]): [description]
        targetP ([type]): [description]
        r ([type]): [description]

    Returns:
        [type]: [description]
    """
    if t1_rad > 1.5707:  #for semisphere
        t1_rad = t1_rad/2
    
    # for reference https://mathinsight.org/spherical_coordinates
    x = targetP[0] + (r * math.sin(t1_rad) * math.cos(t2_rad))
    y = targetP[1] + (r * math.sin(t1_rad) * math.sin(t2_rad))
    z = targetP[2] + (r * math.cos(t1_rad))
    
    quadrant = 0
    
    if 0 >= t2_rad and t2_rad <= 1.5707963267948966:
        quadrant = 1
    elif 1.5882496193148399 >= t2_rad and t2_rad <= 3.141592653589793:
        quadrant = 2
    elif 3.1590459461097367 >= t2_rad and t2_rad <= 4.71238898038469:
        quadrant = 3
    elif 4.729842272904633 >= t2_rad and t2_rad <= 6.283185307179586:
        quadrant = 4
        
    return np.array([[x,y,z],quadrant])

def getSphericalCoords(targetP, radius, angle):
    """[summary]

    Args:
        targetP ([type]): [description]
        radius ([type]): [description]

    Returns:
        [type]: [description]
    """
    stack = []
    stack.append([[targetP[0],targetP[1],targetP[2]+radius],0])
    for i in [angle]:
        for j in [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]:
            val = sphericalRelative(math.radians(i), math.radians(j), targetP, radius)
            stack.append(val)
    return np.array(stack)





