import matplotlib.pyplot as plt
import main_1

RTAP_DATA = main_1.RTAP4_NE
iPhone_DATA = main_1.iPHONE4_NE
Galaxy_DATA = main_1.Galaxy4_NE

if __name__ == "__main__":
    plt.plot(RTAP_DATA[:, 1], RTAP_DATA[:, 0], "or", markersize=3)
    plt.plot(iPhone_DATA[:, 1], iPhone_DATA[:, 0], "og", markersize=3)
    plt.plot(Galaxy_DATA[:, 1], Galaxy_DATA[:, 0], "ob", markersize=3)
    
    plt.plot(sum(RTAP_DATA[:, 1])/len(RTAP_DATA[:, 1]), sum(RTAP_DATA[:, 0])/len(RTAP_DATA[:, 0]), "vk", markersize=2)
    plt.plot(sum(iPhone_DATA[:, 1])/len(iPhone_DATA[:, 1]), sum(iPhone_DATA[:, 0])/len(iPhone_DATA[:, 0]), "vm", markersize=2)
    plt.plot(sum(Galaxy_DATA[:, 1])/len(Galaxy_DATA[:, 1]), sum(Galaxy_DATA[:, 0])/len(Galaxy_DATA[:, 0]), "vc", markersize=2)
    
    E_avg = (sum(RTAP_DATA[:, 1])/len(RTAP_DATA[:, 1]) + sum(iPhone_DATA[:, 1])/len(iPhone_DATA[:, 1]) + sum(Galaxy_DATA[:, 1])/len(Galaxy_DATA[:, 1])) / 3
    N_avg = (sum(RTAP_DATA[:, 0])/len(RTAP_DATA[:, 0]) + sum(iPhone_DATA[:, 0])/len(iPhone_DATA[:, 0]) + sum(Galaxy_DATA[:, 0])/len(Galaxy_DATA[:, 0])) / 3
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("plot at Point 4")
    plt.legend(["RTAP", "iPhone", "Galaxy", "avg of RTAP", "avg of iPhone", "avg of Galaxy"])
    
    plt.xlim(E_avg - 10, E_avg + 10)
    plt.ylim(N_avg - 10, N_avg + 10)
    
    plt.xlabel("E (m)")
    plt.ylabel("N (m)")
    
    plt.show()