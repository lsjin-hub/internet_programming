#오븐 시계
#구이를 시작하는 시각과 하는 데 필요한 시간이 분단위로 주어졌을 때, 끝나는 시간 계산
a,b=map(int,input("").split())
c=int(input(""))

a+=c//60
b+=c%60

a+=b//60
b%=60
a%=24

print("{} {}".format(a,b))