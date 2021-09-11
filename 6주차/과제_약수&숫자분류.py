number=int(input("숫자를 입력하세요 : "))
list_a=[]
total=0
print(number,"의 약수 : ",end='')

for i in range(1,number+1):
    if number%i==0:
        print(i,end=' ')
        list_a.append(i)
        total=total+i

total=total-number
print()

if len(list_a)==2:
    print("숫자 {}은 소수입니다".format(number))
elif total==number:
    print("숫자 {}은 완전수입니다.".format(number))
else:
    print("숫자 {}은 일반수입니다".format(number))