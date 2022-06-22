import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pymap3d as pm
import matplotlib as mpl

GT_DATA = [37.449858691094, 126.651158547171]

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
    f_E, f_N, _ = pm.geodetic2enu(f_N, f_E, 0, GT_DATA[0], GT_DATA[1], 0)

    return f_N, f_E

# with open("nmea/reference_point_umbrella.nmea", "r") as f:
with open("nmea/meeyoongdae+heidaeger_umbrella.nmea", "r") as f:
    ref_lines = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

pre_TOT_DATA = []
pre_ref_point = []
for num, i in enumerate(ref_lines):
    if i[0].strip() == "GNGGA":
        pre_TOT_DATA.append(i)
        pre_ref_point.append(i)
        
REF_POINT_LL = []
TOT_DATA_LL = []

for i in pre_ref_point:
    tmp_lat, tmp_lon = calc_pos_2_LL(i)
    REF_POINT_LL.append([tmp_lat, tmp_lon])

REF_POINT_LL = np.array(REF_POINT_LL)
AVG_REF_LL = np.average(REF_POINT_LL, axis=0)

REF_POINT_NE = []

for i in pre_ref_point:
    N, E = calc_pos_2_NE(i, AVG_REF_LL)
    REF_POINT_NE.append([N, E])

REF_POINT_NE = np.array(REF_POINT_NE)
print(REF_POINT_NE)
AVG_REF_POINT_NE = np.average(REF_POINT_NE, axis=0)
dist_N = abs(min(REF_POINT_NE[:, 0]) - max(REF_POINT_NE[:, 0]))
dist_E = abs(min(REF_POINT_NE[:, 1]) - max(REF_POINT_NE[:, 1]))
dist = dist_N if dist_N > dist_E else dist_E

fontpath = r'C:\Users\1234\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'
font = fm.FontProperties(fname=fontpath, size = 24)
plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)
mpl.font_manager._rebuild()
fm._rebuild()

if __name__ == "__main__":
    plt.plot(REF_POINT_NE[:, 1], REF_POINT_NE[:, 0], "og", markersize=3)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.xlim([AVG_REF_POINT_NE[1] - dist, AVG_REF_POINT_NE[1] + dist])
    plt.ylim([AVG_REF_POINT_NE[0] - dist, AVG_REF_POINT_NE[0] + dist])
    plt.title("미융대+하이데거 (우천)")
    plt.show()