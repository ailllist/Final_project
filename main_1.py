import numpy as np
import matplotlib.pyplot as plt
import pymap3d as pm

# GPS 과제 1을 위한 코드..였지만 이게 진짜임.

def calc_pos_2_LL(string):

    tmp_N_f = float(string[2][:2])
    tmp_N_e = float(string[2][2:]) / 60
    f_Lat = tmp_N_f + tmp_N_e

    tmp_E_f = float(string[4][:3])
    tmp_E_e = float(string[4][3:]) / 60
    f_Lon = tmp_E_f + tmp_E_e

    return f_Lat, f_Lon

def calc_pos_2_NE(string, avgs):

    tmp_N_f = float(string[2][:2])
    tmp_N_e = float(string[2][2:]) / 60
    f_N = tmp_N_f + tmp_N_e

    tmp_E_f = float(string[4][:3])
    tmp_E_e = float(string[4][3:]) / 60
    f_E = tmp_E_f + tmp_E_e
    f_E, f_N, _ = pm.geodetic2enu(f_N, f_E, 0, avgs[0], avgs[1], 0)

    return f_N, f_E

with open("nmea_data/1_square.nmea", "r") as f:
    RTAP1 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/2_square.nmea", "r") as f:
    RTAP2 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/3_square.nmea", "r") as f:
    RTAP3 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/4_square.nmea", "r") as f:
    RTAP4 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/nmea_2.log", "r") as f:
    IPhone1 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/nmea_3.log", "r") as f:
    IPhone2 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/nmea_4.log", "r") as f:
    IPhone3 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/nmea_5.log", "r") as f:
    IPhone4 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/2022-06-21_130524_GPS1.txt", "r") as f:
    Galaxy1 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/2022-06-21_131308_GPS2.txt", "r") as f:
    Galaxy2 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/2022-06-21_132158_GPS3.txt", "r") as f:
    Galaxy3 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

with open("nmea_data/2022-06-21_133507_GPS4.txt", "r") as f:
    Galaxy4 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

TOT_DATA = []
pre_RTAP1 = []
pre_RTAP2 = []
pre_RTAP3 = []
pre_RTAP4 = []
pre_iPhone1 = []
pre_iPhone2 = []
pre_iPhone3 = []
pre_iPhone4 = []
pre_Galaxy1 = []
pre_Galaxy2 = []
pre_Galaxy3 = []
pre_Galaxy4 = []


for num, i in enumerate(RTAP1):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_RTAP1.append(i)

for num, i in enumerate(RTAP2):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_RTAP2.append(i)

for num, i in enumerate(RTAP3):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_RTAP3.append(i)

for num, i in enumerate(RTAP4):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_RTAP4.append(i)

for num, i in enumerate(Galaxy1):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_Galaxy1.append(i)

for num, i in enumerate(Galaxy2):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_Galaxy2.append(i)

for num, i in enumerate(Galaxy3):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_Galaxy3.append(i)

for num, i in enumerate(Galaxy4):
    if i[0].strip() == "GNGGA":
        TOT_DATA.append(i)
        pre_Galaxy4.append(i)

for num, i in enumerate(IPhone1):
    if i[0].strip() == "GPGGA":
        TOT_DATA.append(i)
        pre_iPhone1.append(i)

for num, i in enumerate(IPhone2):
    if i[0].strip() == "GPGGA":
        TOT_DATA.append(i)
        pre_iPhone2.append(i)

for num, i in enumerate(IPhone3):
    if i[0].strip() == "GPGGA":
        TOT_DATA.append(i)
        pre_iPhone3.append(i)

for num, i in enumerate(IPhone4):
    if i[0].strip() == "GPGGA":
        TOT_DATA.append(i)
        pre_iPhone4.append(i)

TOT_DATA_Lat = []
TOT_DATA_Lon = []

RTAP1_NE = []
RTAP2_NE = []
RTAP3_NE = []
RTAP4_NE = []
iPHONE1_NE = []
iPHONE2_NE = []
iPHONE3_NE = []
iPHONE4_NE = []
Galaxy1_NE = []
Galaxy2_NE = []
Galaxy3_NE = []
Galaxy4_NE = []

for i in TOT_DATA:
    tmp_lat, tmp_lon = calc_pos_2_LL(i)
    TOT_DATA_Lat.append(tmp_lat)
    TOT_DATA_Lon.append(tmp_lon)

avg_lat = sum(TOT_DATA_Lat) / len(TOT_DATA_Lat)
avg_lon = sum(TOT_DATA_Lon) / len(TOT_DATA_Lon)
avgs = [avg_lat, avg_lon]

for i in pre_RTAP1:
    N, E = calc_pos_2_NE(i, avgs)
    RTAP1_NE.append([N, E])

for i in pre_RTAP2:
    N, E = calc_pos_2_NE(i, avgs)
    RTAP2_NE.append([N, E])

for i in pre_RTAP3:
    N, E = calc_pos_2_NE(i, avgs)
    RTAP3_NE.append([N, E])

for i in pre_RTAP4:
    N, E = calc_pos_2_NE(i, avgs)
    RTAP4_NE.append([N, E])

for i in pre_iPhone1:
    N, E = calc_pos_2_NE(i, avgs)
    iPHONE1_NE.append([N, E])

for i in pre_iPhone2:
    N, E = calc_pos_2_NE(i, avgs)
    iPHONE2_NE.append([N, E])

for i in pre_iPhone3:
    N, E = calc_pos_2_NE(i, avgs)
    iPHONE3_NE.append([N, E])

for i in pre_iPhone4:
    N, E = calc_pos_2_NE(i, avgs)
    iPHONE4_NE.append([N, E])

for i in pre_Galaxy1:
    N, E = calc_pos_2_NE(i, avgs)
    Galaxy1_NE.append([N, E])

for i in pre_Galaxy2:
    N, E = calc_pos_2_NE(i, avgs)
    Galaxy2_NE.append([N, E])

for i in pre_Galaxy3:
    N, E = calc_pos_2_NE(i, avgs)
    Galaxy3_NE.append([N, E])

for i in pre_Galaxy4:
    N, E = calc_pos_2_NE(i, avgs)
    Galaxy4_NE.append([N, E])

RTAP_NE = []
RTAP_NE.extend(RTAP1_NE)
RTAP_NE.extend(RTAP2_NE)
RTAP_NE.extend(RTAP3_NE)
RTAP_NE.extend(RTAP4_NE)
iPHONE_NE = []
iPHONE_NE.extend(iPHONE1_NE)
iPHONE_NE.extend(iPHONE2_NE)
iPHONE_NE.extend(iPHONE3_NE)
iPHONE_NE.extend(iPHONE4_NE)
Galaxy_NE = []
Galaxy_NE.extend(Galaxy1_NE)
Galaxy_NE.extend(Galaxy2_NE)
Galaxy_NE.extend(Galaxy3_NE)
Galaxy_NE.extend(Galaxy4_NE)

RTAP_NE = np.array(RTAP_NE)
RTAP1_NE = np.array(RTAP1_NE)
RTAP2_NE = np.array(RTAP2_NE)
RTAP3_NE = np.array(RTAP3_NE)
RTAP4_NE = np.array(RTAP4_NE)

iPHONE_NE = np.array(iPHONE_NE)
iPHONE1_NE = np.array(iPHONE1_NE)
iPHONE2_NE = np.array(iPHONE2_NE)
iPHONE3_NE = np.array(iPHONE3_NE)
iPHONE4_NE = np.array(iPHONE4_NE)

Galaxy_NE = np.array(Galaxy_NE)
Galaxy1_NE = np.array(Galaxy1_NE)
Galaxy2_NE = np.array(Galaxy2_NE)
Galaxy3_NE = np.array(Galaxy3_NE)
Galaxy4_NE = np.array(Galaxy4_NE)

if __name__ == "__main__":

    plt.plot(RTAP_NE[:, 1], RTAP_NE[:, 0], "or", markersize=3)
    plt.plot(sum(RTAP_NE[:, 1])/len(RTAP_NE[:, 1]), sum(RTAP_NE[:, 0])/len(RTAP_NE[:, 0]), "vk", markersize=2)
    plt.plot(iPHONE_NE[:, 1], iPHONE_NE[:, 0], "og", markersize=3)
    plt.plot(sum(iPHONE_NE[:, 1]) / len(iPHONE_NE[:, 1]), sum(iPHONE_NE[:, 0]) / len(iPHONE_NE[:, 0]), "vm", markersize=2)
    plt.plot(Galaxy_NE[:, 1], Galaxy_NE[:, 0], "ob", markersize=3)
    plt.plot(sum(Galaxy_NE[:, 1]) / len(Galaxy_NE[:, 1]), sum(Galaxy_NE[:, 0]) / len(Galaxy_NE[:, 0]), "vc",
             markersize=2)
    plt.xlim([-100, 100])
    plt.ylim([-100, 100])
    plt.legend(["RTAP", "center of RTAP", "iPhone", "center of iPhone", "Galaxy", "center of Galaxy"])
    plt.title("all point")
    plt.xlabel("E (m)")
    plt.ylabel("N (m)")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()