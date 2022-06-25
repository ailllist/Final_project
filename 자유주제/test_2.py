import numpy as np

import matplotlib.patches as patches

import matplotlib.pyplot as plt







#circle

shp=patches.Circle((2,2), radius=1, color='r')

plt.gca().add_patch(shp)



#rectangle

shp=patches.Rectangle((2,4), 3,1, color='b')

plt.gca().add_patch(shp)



#ellipse

shp=patches.Ellipse((6,6), 4,1, color='g',angle=45)

plt.gca().add_patch(shp)



plt.show()