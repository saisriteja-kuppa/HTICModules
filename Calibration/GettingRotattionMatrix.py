from scipy.spatial.transform import Rotation as R
 
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def get_euler_from_matrix(angles):
    return R.from_euler('xyz',angles,degrees = True).as_matrix()

def get_matrix_from_euler(mat):
    return R.from_matrix(mat).as_euler('xyz',degrees = True)


T06 = get_euler_from_matrix([-90 , 0 , 90])
T07 = get_euler_from_matrix([-143.098, 28.127, 57.690])

T67 = np.dot(np.linalg.inv(T06),T07)




print('The rotation matrix is')
print(T67, '\n')

print('The Euler angles are \n', get_matrix_from_euler(T67))