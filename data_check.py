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
with open("nmea/2_back_normal.nmea", "r") as f:
    ref_lines = [i.strip("\n").strip("$").split(",") for i in f.readlines()]
with open("nmea/2_back_umbrella.nmea", "r") as f:
    ref_lines1 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

ref_lines.extend(ref_lines1)

pre_TOT_DATA = []
pre_ref_point = []
for num, i in enumerate(ref_lines):
    if i[0].strip() == "GNGGA":
        pre_TOT_DATA.append(i)
        pre_ref_point.append(i)
        
REF_POINT_LL = []
TOT_DATA_LL = []
signal_list = []

for i in pre_ref_point:
    signal_list.append(i[6:8])
    tmp_lat, tmp_lon = calc_pos_2_LL(i)
    REF_POINT_LL.append([tmp_lat, tmp_lon])

print(signal_list)

REF_POINT_LL = np.array(REF_POINT_LL)
AVG_REF_LL = np.average(REF_POINT_LL, axis=0)

REF_POINT_NE = []

for i in pre_ref_point:
    N, E = calc_pos_2_NE(i, AVG_REF_LL)
    REF_POINT_NE.append([N, E])

REF_POINT_NE = np.array(REF_POINT_NE)
AVG_REF_POINT_NE = np.average(REF_POINT_NE, axis=0)
STD_REF_POINT_NE = np.std(REF_POINT_NE, axis=0)

dist_N = abs(min(REF_POINT_NE[:, 0]) - max(REF_POINT_NE[:, 0]))
dist_E = abs(min(REF_POINT_NE[:, 1]) - max(REF_POINT_NE[:, 1]))
dist = dist_N if dist_N > dist_E else dist_E

print(f"전체 평균(NE): {AVG_REF_POINT_NE}")
print(f"전체 표준편차(NE): {STD_REF_POINT_NE}")
print(f"전체 수평범위(E): {dist_E} m")
print(f"전체 수직범위(N): {dist_N} m")

# fontpath = r'C:\Users\1234\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'
fontpath = r'C:\Users\hojun\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'
font = fm.FontProperties(fname=fontpath, size = 24)
plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)
mpl.font_manager._rebuild()
fm._rebuild()

if __name__ == "__main__":
    # plt.plot(REF_POINT_NE[:, 1], REF_POINT_NE[:, 0], "og", markersize=3)
    plt.gca().set_aspect('equal', adjustable='box')
    
    signal_1 = []
    signal_2 = []
    signal_4 = []
    signal_5 = []
    
    for num, i in enumerate(REF_POINT_NE):
        
        if signal_list[num][0] == "1":
            signal_1.append(i)
            
        elif signal_list[num][0] == "2":
            signal_2.append(i)
            
        elif signal_list[num][0] == "4":
            signal_4.append(i)
            
        elif signal_list[num][0] == "5":
            signal_5.append(i)
    
    signal_1 = np.array(signal_1)
    signal_2 = np.array(signal_2)
    signal_4 = np.array(signal_4)
    signal_5 = np.array(signal_5)
    
    lbl_list = []
    
    try:
        plt.plot(signal_1[:, 1], signal_1[:, 0], "or", markersize=3)
        AVG_SIGNAL_1 = np.average(signal_1)
        STD_SIGNAL_1 = np.std(signal_1)
        dist_N1 = abs(min(signal_1[:, 0]) - max(signal_1[:, 0]))
        dist_E1 = abs(min(signal_1[:, 1]) - max(signal_1[:, 1]))
        print(f"")
        lbl_list.append("GNSS fix valid")
    except:
        pass
    
    try:
        plt.plot(signal_2[:, 1], signal_2[:, 0], "om", markersize=3)
        AVG_SIGNAL_2 = np.average(signal_2)
        STD_SIGNAL_2 = np.std(signal_2)
        dist_N2 = abs(min(signal_2[:, 0]) - max(signal_2[:, 0]))
        dist_E2 = abs(min(signal_2[:, 1]) - max(signal_2[:, 1]))
        lbl_list.append("DGPS")
    except:
        pass
    
    try:
        plt.plot(signal_4[:, 1], signal_4[:, 0], "og", markersize=3)
        lbl_list.append("RTK fixed ambiguities")
    except:
        pass
    
    try:
        plt.plot(signal_5[:, 1], signal_5[:, 0], "ob", markersize=3)
        lbl_list.append("RTK float ambiguities")
    except:
        pass
    
    plt.xlim([AVG_REF_POINT_NE[1] - dist, AVG_REF_POINT_NE[1] + dist])
    plt.ylim([AVG_REF_POINT_NE[0] - dist, AVG_REF_POINT_NE[0] + dist])
    plt.title("미융대+하이데거")
    plt.legend(lbl_list)
    plt.show()