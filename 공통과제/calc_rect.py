import pre_calc_rect
import numpy as np
import matplotlib.pyplot as plt

RTAP_data = [pre_calc_rect.RTAP_1, pre_calc_rect.RTAP_2, pre_calc_rect.RTAP_3]
ARR_RTAP_DATA = np.array(RTAP_data)
diff_RTAP_1 = np.array(RTAP_data[0]) - np.array(RTAP_data[1])
diff_RTAP_2 = np.array(RTAP_data[1]) - np.array(RTAP_data[2])

RTAP_norm_1 = np.linalg.norm(diff_RTAP_1)
RTAP_norm_2 = np.linalg.norm(diff_RTAP_2)

print(diff_RTAP_1)
print(np.linalg.norm(diff_RTAP_1))
print(diff_RTAP_2)
print(np.linalg.norm(diff_RTAP_2))

iPhone_data = [pre_calc_rect.iPhone_4, pre_calc_rect.iPhone_1, pre_calc_rect.iPhone_2]
ARR_iPhone_DATA = np.array(iPhone_data)
diff_iPhone_1 = np.array(iPhone_data[0]) - np.array(iPhone_data[1])
diff_iPhone_2 = np.array(iPhone_data[1]) - np.array(iPhone_data[2])

iPhone_norm_1 = np.linalg.norm(diff_iPhone_1)
iPhone_norm_2 = np.linalg.norm(diff_iPhone_2)

print(diff_iPhone_1)
print(np.linalg.norm(diff_iPhone_1))
print(diff_iPhone_2)
print(np.linalg.norm(diff_iPhone_2))

Galaxy_data = [pre_calc_rect.Galaxy_4, pre_calc_rect.Galaxy_1, pre_calc_rect.Galaxy_2]
ARR_Galaxy_DATA = np.array(Galaxy_data)
diff_Galaxy_1 = np.array(Galaxy_data[0]) - np.array(Galaxy_data[1])
diff_Galaxy_2 = np.array(Galaxy_data[1]) - np.array(Galaxy_data[2])

Galaxy_norm_1 = np.linalg.norm(diff_Galaxy_1)
Galaxy_norm_2 = np.linalg.norm(diff_Galaxy_2)

print(diff_Galaxy_1)
print(np.linalg.norm(diff_Galaxy_1))
print(diff_Galaxy_2)
print(np.linalg.norm(diff_Galaxy_2))

if __name__ == "__main__":
    plt.text((Galaxy_data[0][0] + Galaxy_data[1][0])/2 - 30, (Galaxy_data[0][1] + Galaxy_data[1][1])/2 - 15,
             f"{round(Galaxy_norm_1, 5)} m")
    plt.text((Galaxy_data[1][0] + Galaxy_data[2][0])/2 - 30, (Galaxy_data[1][1] + Galaxy_data[2][1])/2 - 15,
             f"{round(Galaxy_norm_2, 5)} m")
    plt.plot(pre_calc_rect.Galaxy_AVG[:, 0], pre_calc_rect.Galaxy_AVG[:, 1], "-or")
    plt.plot(ARR_Galaxy_DATA[:, 0], ARR_Galaxy_DATA[:, 1], "-og")
    plt.xlim([-100, 100])
    plt.ylim([-100, 100])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(["not used line", "used line"])
    plt.xlabel("E (m)")
    plt.ylabel("N (m)")
    plt.title(f"area(Galaxy): {round(Galaxy_norm_1 * Galaxy_norm_2, 5)} m^2")
    plt.show()