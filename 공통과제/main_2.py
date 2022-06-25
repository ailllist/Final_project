import matplotlib.pyplot as plt
import numpy as np
import pymap3d as pm

"""
GPS 자유주제
"""

GT_DATA = [37.45092211414677, 126.65430390610209]
GT_DATA_NE = pm.geodetic2enu(GT_DATA[0], GT_DATA[1], 0, GT_DATA[0], GT_DATA[1], 0)

def calc_pos(string):

    tmp_N_f = float(string[2][:2])
    tmp_N_e = float(string[2][2:]) / 60
    f_N = tmp_N_f + tmp_N_e

    tmp_E_f = float(string[4][:3])
    tmp_E_e = float(string[4][3:]) / 60
    f_E = tmp_E_f + tmp_E_e
    f_N, f_E, _ = pm.geodetic2enu(f_N, f_E, 0, GT_DATA[0], GT_DATA[1], 0)

    return f_N, f_E

def calc_avg(NE_list: np.ndarray):

    tot_n = NE_list[:, 0]
    tot_e = NE_list[:, 1]

    avg_n = sum(tot_n) / len(tot_n)
    avg_e = sum(tot_e) / len(tot_e)

    dist_n = max(tot_n) - min(tot_n)
    dist_e = max(tot_e) - min(tot_e)

    return [avg_n, avg_e], [dist_n, dist_e]


with open("nmea_2.log", "r", encoding="utf-8") as f:
    lines1 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

RTAP1 = []

for num, i in enumerate(lines1):
    if i[0].strip() == "GNGGA":
        RTAP1.append(i)

RTAP1_NE = [] # RTAP의 부분적인 N, E 좌표
RTAP_NE = [] # RTAP의 전체 N, E 좌표

for i in RTAP1:

    f_N, f_E = calc_pos(i)

    RTAP1_NE.append([f_N, f_E])
    RTAP_NE.append([f_N, f_E])

RTAP1_NE = np.array(RTAP1_NE)
RTAP_NE = np.array(RTAP_NE)

avgs, dists = calc_avg(RTAP_NE)

dist = dists[0] if dists[0] > dists[1] else dists[1]

if __name__ == "__main__":
    plt.plot(RTAP_NE[:, 0], RTAP_NE[:, 1], "ob")
    plt.plot(GT_DATA_NE[0], GT_DATA_NE[1], "or")
    # plt.xlim([avgs[0] - dist, avgs[0] + dist])
    # plt.ylim([avgs[1] - dist, avgs[1] + dist])

    plt.show()