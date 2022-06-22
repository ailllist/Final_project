import main_1
import numpy as np

RTAP1 = main_1.Galaxy4_NE # N, E
RTAP1_AVG = np.average(RTAP1, axis=0)
print(RTAP1 - RTAP1_AVG)

if __name__ == "__main__":
    pass