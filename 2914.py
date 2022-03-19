#저작권
#(앨범에 수록된 곡에 포함되어 있는 저작권이 있는 멜로디의 개수) / (앨범에 수록된 곡의 개수)
#평균값은 항상 올림을 해서 정수로 만들어야 한다.

album, ave=map(int,input("").split())
min=album*(ave-1)+1

print(min)