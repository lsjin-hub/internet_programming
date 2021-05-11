#나머지
#(A+B)%C ((A%C)+(B%C))%C
#(AXB)%C ((A%C)X(B%C))%C

a,b,c=map(int, input("").split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)