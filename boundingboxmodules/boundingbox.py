import numpy as np
import plotly.express as px
import pandas as pd



x_low,x_high,y_low,y_high,z_low,z_high = 0,0,0,0,0,0
x_distance, y_distance, z_distance = 0,0,0


def getboxpoints(diagonalp1, diagonalp2, threshold):
    
    x_distance, y_distance, z_distance = threshold
    
    x_min, x_max = min(diagonalp1[0],diagonalp2[0]), max(diagonalp1[0],diagonalp2[0])
    y_min, y_max = min(diagonalp1[1], diagonalp2[1]), max(diagonalp1[1], diagonalp2[1])
    z_min, z_max = min(diagonalp1[2], diagonalp2[2]), max(diagonalp1[2], diagonalp2[2])
    
    x_thresh = np.arange(x_min, x_max, x_distance)
    y_thresh = np.arange(y_min, y_max, y_distance)
    z_thresh = np.arange(z_min, z_max, z_distance)

    X, Y, Z = np.meshgrid(x_thresh, y_thresh, z_thresh)
    X,Y,Z = X.flatten(), Y.flatten(), Z.flatten()
        
    return X,Y,Z


def plotpoints(points, status, filter = None):
    
    'good for true, bad for false'
    
    X,Y,Z = points
    
    data  = {'x':X, 'y':Y, 'z':Z, 'status':status}
    df = pd.DataFrame(data)
    
    print(df.loc[df['status']== True])
    if filter == True: df = df.loc[df['status']== 'good']
    if filter == False: df = df.loc[df['status']== 'bad']

    # if filter == None:
    fig = px.scatter_3d(df, x='x', y='y', z='z',
                color='status')

    fig.show()
    
    

#sample code to check    
points = getboxpoints([100,100,100], [20,150,90], [2,2,0.5])

if np.array(points).shape[1] %2 == 0.0:
    status_list = ['good']*(len(points[0])//2) + ['bad']*(len(points[0])//2)
else:
    status_list = ['False'] + ['good']*(len(points[0])//2) + ['bad']*(len(points[0])//2) 
print(np.array(points).shape, len(status_list))

import random
random.shuffle(status_list)
plotpoints(points, status_list, filter= None)



