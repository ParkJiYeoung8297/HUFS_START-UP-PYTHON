date=input("달력을 원하는 해와 달을 입력해주세요(해.월):").split('.')
#date 리스트가 문자(string)으로 입력 받았으니 그걸 int 로 형 변환 시킴
for i in range(len(date)):
    date[i]=int(date[i])

input_day=input("첫째날은 몇 요일인가요?(MON/TUE/WED/THU/FRI/SAT/SUN):  ")
month1=[1,3,5,7,8,10,12]
month2=[2,4,6,9,11]
#날짜수 정하기
if date[1]==2:
    if (date[0]/4==0&date[0]/100!=0) or date[0]/400==0: #and 대신 &써야한다고 에러떠서 &로 바꿈
        num=29
    else:
        num=28
elif date[1] in month1: #month1 리스트에 있는 월이면 31일 이라는 뜻
    num=31
elif date[1] in month2:
    num=30
else:
    print("잘못된 입력입니다")

print('            {}              '.format(date[1]))
print('SUN MON TUE WED THU FRI SAT')

dictionary={
    'SUN':'7', #쉼표 없으면 에러뜸
    'MON':'6',
    'TUE':'5',
    'WED':'4',
    'THU':'3',
    'FRI':'2',
    'SAT':'1'
}
 #첨에는 리스트로 하려 햇으나 그러면 [1,2,3,]이런식으로 출력되서 그냥 리스트안쓰기로 함
    #시작하는 요일에 따라 다르게 하기(첫줄)
    
if input_day=='SUN': #문자도 같은지 볼떄 ==인듯(자바랑 다름)
    for i in range(num):
        if (i+1)%7==0:
            if(i+1)<10:
                print("  {}".format(i+1))#줄바꾸기
            else:
                print(" {}".format(i+1))

        else:
            if (i+1)<10:
                print("  {}".format(i+1),end=" ")#줄 안바꾸기
            else:
                print(" {}".format(i+1),end=" ")
        
elif input_day=='MON':
    print("      1",end=" ")
    for i in range(num-1):#i=0에서 시작,for 문 시작은 2일부터임,위에서 1일 했으니까
        if (i+3)%7==0:#화욜이 2일 i=0인 상태
            if(i+2)<10:#2일이 시작 기준이니까 +2해서 맞춰줌
                print("  {}".format(i+2))
            else:
                print(" {}".format(i+2))

        else:
            if (i+2)<10:
                print("  {}".format(i+2),end=" ")
            else:
                print(" {}".format(i+2),end=" ")

elif input_day=='TUE': 
    print("          1",end=" ")
    for i in range(num-1):
        if (i+4)%7==0:
            if(i+2)<10:
                print("  {}".format(i+2))
            else:
                print(" {}".format(i+2))

        else:
            if (i+2)<10:
                print("  {}".format(i+1),end=" ")
            else:
                print(" {}".format(i+1),end=" ")

elif input_day=='WED': 
    print("              1",end=" ")
    for i in range(num-1):
        if (i+5)%7==0:
            if(i+2)<10:
                print("  {}".format(i+2))
            else:
                print(" {}".format(i+2))

        else:
            if (i+2)<10:
                print("  {}".format(i+2),end=" ")
            else:
                print(" {}".format(i+2),end=" ")
elif input_day=='THU': 
    print("                  1",end=" ")
    for i in range(num-1):
        if (i+6)%7==0:
            if(i+2)<10:
                print("  {}".format(i+2))
            else:
                print(" {}".format(i+2))

        else:
            if (i+2)<10:
                print("  {}".format(i+2),end=" ")
            else:
                print(" {}".format(i+2),end=" ")
elif input_day=='FRI': 
    print("                      1",end=" ")
    for i in range(num-1):
        if (i+7)%7==0:
            if(i+2)<10:
                print("  {}".format(i+2))
            else:
                print(" {}".format(i+2))

        else:
            if (i+2)<10:
                print("  {}".format(i+2),end=" ")
            else:
                print(" {}".format(i+2),end=" ")

elif input_day=='SAT': 
    print("                          1",end=" ")
    for i in range(num-1):
        if (i+1)%7==0:
            if(i+1)<10:
                print("  {}".format(i+2))
            else:
                print(" {}".format(i+2))

        else:
            if (i+1)<10:
                print("  {}".format(i+2),end=" ")
            else:
                print(" {}".format(i+2),end=" ")