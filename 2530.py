#2530
#인공지능 시계
#훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 초 단위로 주어졌을 때,
#오븐구이가 끝나는 시각을 계산하는 프로그램

hour, min, sec=map(int,input("").split())
cooktime=int(input(""))

sec+=cooktime  
min+=sec//60  
hour+=min//60

hour%=24
min%=60
sec%=60

print("{} {} {}".format(hour,min,sec))