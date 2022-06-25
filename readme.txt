조원: 이호준(팀장), 김종학, 이승우
이 자료는 2022년도 봄학기 GPS개론 기말 프로젝트의 코드 자료물로서 다음과 같은 구성을 가집니다.
공통과제
└ nmea_data
    └ *.nmea : 저희가 공통과제를 수행하면서 수집한 데이터입니다.
└ calc_avgs.py : dxdy(dNdE) 를 계산하는 코드입니다.
└ calc_rect.py : 사각형의 면적 계산에 필요한 기로&세로 길이와 면적 값을 계산하고, 이를 plot하는 코드입니다.
└ dxdy_Galaxy.txt : calc_avgs.py로 구한 갤럭시의 데이터입니다.
└ dxdy_iPhone.txt : calc_avgs.py로 구한 아이폰의 데이터입니다.
└ dxdy_RTAP.txt : calc_avgs.py로 구한 RTAP의 데이터입니다.
└ main_1.py : .nmea 파일로 부터 위도, 경도를 불러오고, NED좌표계로 데이터를 가공하는 코드
└ main_1_prev.py : main_1.py의 이전 코드
└ main_2.py : 특정 꼭짓점에서의 특정 장치의 데이터 확인을 위한 코드
└ plot_each_part.py : 특정 꼭짓점에서의 모든 장치 관측값을 plot하고, 각각의 데이터별 표준 편차와 RTAP과의 오차를 구한다.
└ pre_calc_rect.py : 측위 데이터를 바탕으로 직사각형을 plot한다.
└ tmp.py : 과제를 수행하면서 일시적으로 필요한 코딩을 한 파일, 작성시점에서는 평균 LLH좌표가 기록되어있다.


자유주제
└ Figure
    └ *.png : Quality Indicator별 plot된 측위데이터
    └ *.txt : Quality Indicator별 상세 관측 데이터
└ Figure_fixed
    └ *.png : Quality Indicator별 보정된 plot
    └ *.txt : Quality Indicator별 보정 정보(직사각형 면적, 원 면적, 면적 차이)
└ nmea
    └ *.nmea : 자유주제에서 측정한 데이터
└ data_check.py : Quality Indicator별 plot과 표준편차
└ example_*.png : PPT에 사용된 예시 사진
└ plot_circle.py : 보정에 사용한 원과 사각형을 그리고, 면적오차를 구하는 코드
└ test.py : matplotlib에서 한글을 쓸 수 있도록 하는 코드
└ test_2.py : 원과 사각형을 그려본 코드

Round_Calculator.m : N,E좌표를 RGB척도로 변경하는 코드
Rec_Area_Calculation.m : 사각형을 신발끈 공식으로 구하는 코드
