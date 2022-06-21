import main_1
import numpy as np

RTAP1 = []
RTAP2 = []
RTAP3 = []
RTAP4 = []

Galaxy1 = []
Galaxy2 = []
Galaxy3 = []
Galaxy4 = []

iPhone1 = []
iPhone2 = []
iPhone3 = []
iPhone4 = []

for i in main_1.pre_RTAP1:
    lat, lon = main_1.calc_pos_2_LL(i)
    RTAP1.append([lat, lon])

for i in main_1.pre_RTAP2:
    lat, lon = main_1.calc_pos_2_LL(i)
    RTAP2.append([lat, lon])

for i in main_1.pre_RTAP3:
    lat, lon = main_1.calc_pos_2_LL(i)
    RTAP3.append([lat, lon])

for i in main_1.pre_RTAP4:
    lat, lon = main_1.calc_pos_2_LL(i)
    RTAP4.append([lat, lon])

for i in main_1.pre_iPhone1:
    lat, lon = main_1.calc_pos_2_LL(i)
    iPhone1.append([lat, lon])

for i in main_1.pre_iPhone2:
    lat, lon = main_1.calc_pos_2_LL(i)
    iPhone2.append([lat, lon])

for i in main_1.pre_iPhone3:
    lat, lon = main_1.calc_pos_2_LL(i)
    iPhone3.append([lat, lon])

for i in main_1.pre_iPhone4:
    lat, lon = main_1.calc_pos_2_LL(i)
    iPhone4.append([lat, lon])

for i in main_1.pre_Galaxy1:
    lat, lon = main_1.calc_pos_2_LL(i)
    Galaxy1.append([lat, lon])

for i in main_1.pre_Galaxy2:
    lat, lon = main_1.calc_pos_2_LL(i)
    Galaxy2.append([lat, lon])

for i in main_1.pre_Galaxy3:
    lat, lon = main_1.calc_pos_2_LL(i)
    Galaxy3.append([lat, lon])

for i in main_1.pre_Galaxy4:
    lat, lon = main_1.calc_pos_2_LL(i)
    Galaxy4.append([lat, lon])

RTAP1 = np.array(RTAP1)
RTAP2 = np.array(RTAP2)
RTAP3 = np.array(RTAP3)
RTAP4 = np.array(RTAP4)

AVG_RTAP_LL = np.array([np.average(RTAP1, axis=0), np.average(RTAP2, axis=0),
                     np.average(RTAP3, axis=0), np.average(RTAP4, axis=0)])

iPhone1 = np.array(iPhone1)
iPhone2 = np.array(iPhone2)
iPhone3 = np.array(iPhone3)
iPhone4 = np.array(iPhone4)

AVG_iPhone_LL = np.array([np.average(iPhone1, axis=0), np.average(iPhone2, axis=0),
                       np.average(iPhone3, axis=0), np.average(iPhone4, axis=0)])

Galaxy1 = np.array(Galaxy1)
Galaxy2 = np.array(Galaxy2)
Galaxy3 = np.array(Galaxy3)
Galaxy4 = np.array(Galaxy4)

AVG_Galaxy_LL = np.array([np.average(Galaxy1, axis=0), np.average(Galaxy2, axis=0),
                       np.average(Galaxy3, axis=0), np.average(Galaxy4, axis=0)])

if __name__ == "__main__":
    print("RTAP: ", AVG_RTAP_LL)
    print("iPhone: ", AVG_iPhone_LL)
    print("Galaxy: ", AVG_Galaxy_LL)
