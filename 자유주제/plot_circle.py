import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.patches as pth
import numpy as np
import pymap3d as pm
import math

GT_DATA = [37.449858691094, 126.651158547171]


def calc_pos_2_LL(string): # 위도 경도를 추출하는 함수
    tmp_N_f = float(string[2][:2])
    tmp_N_e = float(string[2][2:]) / 60
    f_Lat = tmp_N_f + tmp_N_e

    tmp_E_f = float(string[4][:3])
    tmp_E_e = float(string[4][3:]) / 60
    f_Lon = tmp_E_f + tmp_E_e

    return f_Lat, f_Lon


def calc_pos_2_NE(string, avgs): # N, E를 추출하는 함수
    tmp_N_f = float(string[2][:2])
    tmp_N_e = float(string[2][2:]) / 60
    f_N = tmp_N_f + tmp_N_e

    tmp_E_f = float(string[4][:3])
    tmp_E_e = float(string[4][3:]) / 60
    f_E = tmp_E_f + tmp_E_e
    f_E, f_N, _ = pm.geodetic2enu(f_N, f_E, 0, GT_DATA[0], GT_DATA[1], 0)

    return f_N, f_E


def calc_plt_info(*args): # 원, 사각형 등 그래프를 그리는데 필요한 정보를 추출하는 함수
    tot_data = []
    for i in args:
        for j in i:
            tot_data.append(j)
    tot_data = np.array(tot_data)

    avg_tot_data = np.average(tot_data, axis=0)
    dist_tN = abs(min(tot_data[:, 0]) - max(tot_data[:, 0]))
    dist_tE = abs(min(tot_data[:, 1]) - max(tot_data[:, 1]))
    dist_t3D = (dist_tN ** 2 + dist_tE ** 2) ** (1 / 2)
    t_circle = pth.Circle((avg_tot_data[1], avg_tot_data[0]), radius=dist_t3D/2, fill=False, color="red")
    td_left = [avg_tot_data[0] - dist_tN/2, avg_tot_data[1] - dist_tE/2]
    t_rect = pth.Rectangle((td_left[1], td_left[0]), dist_tE, dist_tN, edgecolor="blue", fill=False)
    info_data = [tot_data, avg_tot_data, dist_tN, dist_tE, dist_t3D] # N, E
    return info_data, t_circle, t_rect


title_name = r"Only DGPS" # 1 4 5
# title_name = r"DGPS + RTK_fixed + RTK_float" # 1 4 5
with open("nmea/kimhyuntae+heidaeger_normal.nmea", "r") as f:
    ref_lines = [i.strip("\n").strip("$").split(",") for i in f.readlines()]
with open("nmea/kimhyuntae+heidaeger_normal_2.nmea", "r") as f:
    ref_lines1 = [i.strip("\n").strip("$").split(",") for i in f.readlines()]

# f = open(f"Figure/{title_name}.txt", "w", encoding="utf-8")
print(title_name)

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

REF_POINT_LL = np.array(REF_POINT_LL)
AVG_REF_LL = np.average(REF_POINT_LL, axis=0)

REF_POINT_NE = []
signal_info = []

for i in pre_ref_point:
    N, E = calc_pos_2_NE(i, AVG_REF_LL)
    signal_info.append(i[6:8])
    REF_POINT_NE.append([N, E])
# print(signal_info)

REF_POINT_NE = np.array(REF_POINT_NE)
AVG_REF_POINT_NE = np.average(REF_POINT_NE, axis=0)
STD_REF_POINT_NE = np.std(REF_POINT_NE, axis=0)

dist_N = abs(min(REF_POINT_NE[:, 0]) - max(REF_POINT_NE[:, 0]))
dist_E = abs(min(REF_POINT_NE[:, 1]) - max(REF_POINT_NE[:, 1]))
dist = dist_N if dist_N > dist_E else dist_E


# fontpath = r'C:\Users\1234\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'
# fontpath = r'C:\Users\hojun\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'
fontpath = r'C:\Users\Autonav-Linux\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'

font = fm.FontProperties(fname=fontpath, size=24)
plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)
# matplotlib.font_manager.rebuild()
# mpl.font_manager._rebuild()
# fm._rebuild()

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
        AVG_SIGNAL_1 = np.average(signal_1, axis=0)
        dist_N1 = abs(min(signal_1[:, 0]) - max(signal_1[:, 0]))
        dist_E1 = abs(min(signal_1[:, 1]) - max(signal_1[:, 1]))
        dist_3D1 = (dist_N1 ** 2 + dist_E1 ** 2) ** (1 / 2)
        print(1)
        lbl_list.append("GNSS fix valid")
    except:
        pass

    try:
        plt.plot(signal_2[:, 1], signal_2[:, 0], "om", markersize=3)
        AVG_SIGNAL_2 = np.average(signal_2, axis=0)
        dist_N2 = abs(min(signal_2[:, 0]) - max(signal_2[:, 0]))
        dist_E2 = abs(min(signal_2[:, 1]) - max(signal_2[:, 1]))
        dist_3D2 = (dist_N2 ** 2 + dist_E2 ** 2) ** (1 / 2)
        print(2)
        lbl_list.append("DGPS")
    except:
        pass

    try:
        plt.plot(signal_4[:, 1], signal_4[:, 0], "og", markersize=3)
        AVG_SIGNAL_4 = np.average(signal_4, axis=0)
        dist_N4 = abs(min(signal_4[:, 0]) - max(signal_4[:, 0]))
        dist_E4 = abs(min(signal_4[:, 1]) - max(signal_4[:, 1]))
        dist_3D4 = (dist_N4 ** 2 + dist_E4 ** 2) ** (1 / 2)
        print(4)
        lbl_list.append("RTK fixed ambiguities")
    except:
        pass

    try:
        plt.plot(signal_5[:, 1], signal_5[:, 0], "ob", markersize=3)
        AVG_SIGNAL_5 = np.average(signal_5, axis=0)
        dist_N5 = abs(min(signal_5[:, 0]) - max(signal_5[:, 0]))
        dist_E5 = abs(min(signal_5[:, 1]) - max(signal_5[:, 1]))
        dist_3D5 = (dist_N5 ** 2 + dist_E5 ** 2) ** (1 / 2)
        print(5)
        lbl_list.append("RTK float ambiguities")
    except:
        pass

    # info_data, circle, rect = calc_plt_info(signal_1, signal_2, signal_4, signal_5)
    # info_data, circle, rect = calc_plt_info(signal_4, signal_5)
    plt.plot(AVG_SIGNAL_4[1], AVG_SIGNAL_4[0], "Xc", markersize=5)
    lbl_list.append("average pos using RTAP")
    info_data, circle, rect = calc_plt_info(signal_2)
    # info_data, circle, rect = calc_plt_info(signal_5)
    circle_area = math.pi * ((info_data[4]/2)**2)
    center_of_rect = info_data[1]
    print("dist of center: ", np.linalg.norm(center_of_rect-AVG_SIGNAL_4), "(m)")
    rect_area = info_data[2] * info_data[3]
    # td_left = [info_data[1][0] - info_data[2]/3, info_data[1][1] - info_data[3]/3]
    # rect2_area = pth.Rectangle((td_left[1], td_left[0]), info_data[3]/1.5, info_data[2]/1.5, edgecolor="yellow", fill=False)
    # plt.gca().add_patch(rect2_area)
    # print(info_data)
    print("원 넓이: ", circle_area, "(m)")
    print("직사각형 넓이: ", rect_area, "(m)")
    print("넓이 차이: ", rect_area-circle_area, "(m)")

    # circle = pth.Circle((AVG_REF_POINT_NE[1], AVG_REF_POINT_NE[0]), radius=dist_3D/2, fill=False, color="red")
    plt.gca().add_patch(circle)
    #
    # d_left = [AVG_REF_POINT_NE[0] - dist_N/2, AVG_REF_POINT_NE[1] - dist_E/2]
    # rect = pth.Rectangle((d_left[1], d_left[0]), dist_E, dist_N, edgecolor="blue", fill=False)
    plt.gca().add_patch(rect)
    dist = info_data[2] if info_data[2] > info_data[3] else info_data[3]

    plt.xlim([info_data[1][1] - dist, info_data[1][1] + dist])
    plt.ylim([info_data[1][0] - dist, info_data[1][0] + dist])
    plt.title(title_name)

    plt.xlabel("E (m)")
    plt.ylabel("N (m)")
    plt.legend(lbl_list)
    # plt.savefig(fr'Figure\{title_name}.png', dpi=300)
    plt.show()