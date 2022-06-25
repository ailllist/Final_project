import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib as mpl

# fontpath = r'C:\Windows\Fonts\NanumSquareR.ttf'
fontpath = r'C:\Users\Autonav-Linux\AppData\Local\Microsoft\Windows\Fonts\NanumGothic.ttf'
font = fm.FontProperties(fname=fontpath, size = 24)
plt.rc('font', family='NanumMyeongjo')
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'r'
plt.rcParams['axes.grid'] = True
# mpl.font_manager._rebuild()
# fm._rebuild()
#
# from matplotlib import font_manager
# for i in font_manager.fontManager.ttflist:
#     if 'Nanum' in i.name:
#         print(i.name, i.fname)