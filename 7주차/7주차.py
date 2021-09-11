#import function
#환율 계산
#function.currency(1000,"미국")

#factorial
def factorial(n):
    total=1 #total은 연산하는 거니까 함수 안에서 한번 정의해주기(안하면 unbounded 오류뜸)
    for i in range(n):#0이상 n미만 범위니까 5번 하는거 i는 0부터 시작
        num=i+1
        total=total*num
    return total

print(factorial(5))

#재귀함수(위에 factorial이랑 같은 게산과정임)
def factorial_r(n):
    if n==0:
        return 1
    else:                                       #▽요 마지막 1은 n==0일때 return 1이므로 마지막 1이 있는거임
        return n*factorial_r(n-1) #5*(4*(3*(2*(1*(1))))) 요런식으로 계산하는거임,그래서 결국 factorial 계산과정&결과와 같음
print(factorial_r(5))


#피보나치 수열
#1 1 2 3 5 8 11...
#n번째 수는 n-1번째 숫자에다가 n-2번째 숫자를 더한 수
#f1=1 f2=1 fn=fn-1 + fn-1
#4번째:4,3,
#5번째:5,4,3,
#6번쨰:6,5,4,3,
def fibonacci(m): #피보나치 수열에서 m번째 있는 수
    fibo=[1,1]
    if m==1:
        return 1
    elif m==2:
        return 1
    else :
        for i in range(1,m-1): #앞에 이미 [1,1]있으므로 1이상 m-1미만까지,i=1부터시작
            temp=fibo[i]+fibo[i-1]             # ↘ 걍range(m-2)하면 반복횟수는 같지만 i=0부터 시작이라 값이 다름
            fibo.append(temp)
        return fibo[m-1]
print(fibonacci(6))

#피보나치 수열을 재귀함수 이용하여 더 심플하게 나타내기
def fibonacci_r(m):
    if m==1:
        return 1
    elif m==2:
        return 1
    else:
        return fibonacci_r(m-1)+fibonacci_r(m-2)
print(fibonacci_r(6))

#가위바위보 ,난수:숫자를 지멋대로 생성
import random #libary 에서 random 함수 쓰려면 import 해야함
print(random.random())
#random():0~1사이 소수를 무작위로 생성하는 함수
print(int(random.random()*1000))
#randrange(max)
#randrange(이상,미만)
print(random.randrange(100))#100미만 
print(random.randrange(10,100))#10이상 100미만

print("컴퓨터와 함께하는 가위바위보")
list_a=["가위","바위","보"]

computer=random.choice(list_a)
user=input()

print(f"사용자: {user}/ 컴퓨터: {computer}")
if user=="가위": 
    if computer=="가위":
        print("무승부입니다")
    elif computer=="바위":
        print("당신이 이겼습니다!")
    elif computer=="보":
        print("당신이 졌습니다ㅠ")
elif user=="바위": 
    if computer=="바위":
        print("무승부입니다")
    elif computer=="보":
        print("당신이 이겼습니다!")
    elif computer=="가위":
        print("당신이 졌습니다ㅠ")
elif user=="보": 
    if computer=="보":
        print("무승부입니다")
    elif computer=="가위":
        print("당신이 이겼습니다!")
    elif computer=="바위":
        print("당신이 졌습니다ㅠ")
else:
    print("가위,바위,보를 입력해주세요!")

#위는 내가 다르게 쓴거고 아래는 선생님이 한 예시 답변

# import random # 내가 쓴 가윕바위보에서 이미 random 함수를 import 했으니까 다시 안써도 됨
print("<컴퓨터와 함께하는 가위바위보>")
#list_a = ["가위", "바위", "보"]

computer = random.choice(list_a)
user = input("가위바위보! ")
print(f"사용자: {user}/ 컴퓨터: {computer}")
if user == "가위" and computer == "가위":
    print("무승부 입니다!")
elif user == "가위" and computer == "바위":
    print("당신이 졌습니다!")
elif user == "가위" and computer == "보":
    print("당신이 이겼습니다!")
elif user == "바위" and computer == "가위":
    print("당신이 이겼습니다!")
elif user == "바위" and computer == "바위":
    print("무승부 입니다!")
elif user == "바위" and computer == "보":
    print("당신이 졌습니다!")
elif user == "보" and computer == "가위":
    print("당신이 졌습니다!")
elif user == "보" and computer == "바위":
    print("당신이 이겼습니다!")
elif user == "보" and computer == "보":
    print("무승부 입니다!")
else :
    print("가위, 바위, 보를 입력해주세요!")