#Q1
a=80
b=75
c=55

print((a+b+c)/3)

#Q2
if 13%2==0:
    print("짝수")
else:
    print("홀수")

#Q3
pin="881120-1068234".split("-")
print(pin)

#Q4
pin="881120-1068234".split("-")

if pin[1][0]=="1" or pin[1][0]=="3":
    print("남자")
else:
    print("여자")

#Q5
a="a:b:c:d".replace(":","#")
print(a)

#Q6
list_a=[1,3,5,4,2]
list_a.sort()
list_a.reverse()
print(list_a)

#Q7
a=['Life', 'is', 'too', 'short']
print (" ".join(a))

#Q8
a=(1,2,3)
a=a+(4,)
print(a)

#Q9

#Q10
a={'A':90, 'B':80, 'C':70}
result=a.pop('B')
print(a)
print(result)