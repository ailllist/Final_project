import matplotlib.pyplot as plt
import numpy as np
import main_1

TOT_ARR = []

RTAP_1 = [sum(main_1.RTAP1_NE[:, 1])/len(main_1.RTAP1_NE[:, 1]), sum(main_1.RTAP1_NE[:, 0])/len(main_1.RTAP1_NE[:, 0])]
RTAP_2 = [sum(main_1.RTAP2_NE[:, 1])/len(main_1.RTAP2_NE[:, 1]), sum(main_1.RTAP2_NE[:, 0])/len(main_1.RTAP2_NE[:, 0])]
RTAP_3 = [sum(main_1.RTAP3_NE[:, 1])/len(main_1.RTAP3_NE[:, 1]), sum(main_1.RTAP3_NE[:, 0])/len(main_1.RTAP3_NE[:, 0])]
RTAP_4 = [sum(main_1.RTAP4_NE[:, 1])/len(main_1.RTAP4_NE[:, 1]), sum(main_1.RTAP4_NE[:, 0])/len(main_1.RTAP4_NE[:, 0])]
RTAP_AVG = [RTAP_1, RTAP_2, RTAP_3, RTAP_4]

iPhone_1 = [sum(main_1.iPHONE1_NE[:, 1])/len(main_1.iPHONE1_NE[:, 1]), sum(main_1.iPHONE1_NE[:, 0])/len(main_1.iPHONE1_NE[:, 0])]
iPhone_2 = [sum(main_1.iPHONE2_NE[:, 1])/len(main_1.iPHONE2_NE[:, 1]), sum(main_1.iPHONE2_NE[:, 0])/len(main_1.iPHONE2_NE[:, 0])]
iPhone_3 = [sum(main_1.iPHONE3_NE[:, 1])/len(main_1.iPHONE3_NE[:, 1]), sum(main_1.iPHONE3_NE[:, 0])/len(main_1.iPHONE3_NE[:, 0])]
iPhone_4 = [sum(main_1.iPHONE4_NE[:, 1])/len(main_1.iPHONE4_NE[:, 1]), sum(main_1.iPHONE4_NE[:, 0])/len(main_1.iPHONE4_NE[:, 0])]
iPhone_AVG = [iPhone_1, iPhone_2, iPhone_3, iPhone_4]

Galaxy_1 = [sum(main_1.Galaxy1_NE[:, 1])/len(main_1.Galaxy1_NE[:, 1]), sum(main_1.Galaxy1_NE[:, 0])/len(main_1.Galaxy1_NE[:, 0])]
Galaxy_2 = [sum(main_1.Galaxy2_NE[:, 1])/len(main_1.Galaxy2_NE[:, 1]), sum(main_1.Galaxy2_NE[:, 0])/len(main_1.Galaxy2_NE[:, 0])]
Galaxy_3 = [sum(main_1.Galaxy3_NE[:, 1])/len(main_1.Galaxy3_NE[:, 1]), sum(main_1.Galaxy3_NE[:, 0])/len(main_1.Galaxy3_NE[:, 0])]
Galaxy_4 = [sum(main_1.Galaxy4_NE[:, 1])/len(main_1.Galaxy4_NE[:, 1]), sum(main_1.Galaxy4_NE[:, 0])/len(main_1.Galaxy4_NE[:, 0])]
Galaxy_AVG = [Galaxy_1, Galaxy_2, Galaxy_3, Galaxy_4]

TOT_ARR.extend(RTAP_AVG)
TOT_ARR.extend(iPhone_AVG)
TOT_ARR.extend(Galaxy_AVG)

RTAP_AVG = np.array(RTAP_AVG)
iPhone_AVG = np.array(iPhone_AVG)
Galaxy_AVG = np.array(Galaxy_AVG)
TOT_ARR = np.array(TOT_ARR)
avg_E = sum(TOT_ARR[:, 0])/len(TOT_ARR[:, 0])
avg_N = sum(TOT_ARR[:, 1])/len(TOT_ARR[:, 1])

if __name__ == "__main__":
    
    plt.plot(RTAP_AVG[:, 0], RTAP_AVG[:, 1], "-or", markersize=3)
    plt.plot(iPhone_AVG[:, 0], iPhone_AVG[:, 1], "-og", markersize=3)
    plt.plot(Galaxy_AVG[:, 0], Galaxy_AVG[:, 1], "-ob", markersize=3)
    plt.legend(["Rect of RTAP", "Rect of iPhone", "Rect of Galaxy"])
    plt.title("Rectangle at all case")
    plt.xlabel("E (m)")
    plt.ylabel("N (m)")
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
    print("RTAP: ", RTAP_AVG)
    print("iPhone: ", iPhone_AVG)
    print("Galaxy: ", Galaxy_AVG)