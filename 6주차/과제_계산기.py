n,m=input("두개의 숫자를 입력하세요 : ").split()
n=int(n)
m=int(m)
operator=input("연산자를 입력하세요 : ")
#(1)함수 이용
def plus(n,m):
    result=n+m
    return result

def minus(n,m):
    if n>m:
        result=n-m
    else:
        result=m-n
    return result

def multiple(n,m):
    result=n*m
    return result

def division_a(n,m):
    if m!=0:
        result=n/m
    else:
        print("0으로 나눌 수 없습니다")
    return result

def division_b(n,m):
    if m!=0:
        result=n//m
    else:
        print("0으로 나눌 수 없습니다")
    return result

def division_c(n,m):
    if m!=0:
        result=n%m
    else:
        print("0으로 나눌 수 없습니다")
    return result


if operator=='+':
    print("뎃셈결과 : ",plus(n,m))
elif operator=='-':
    print("뺄셈결과 : ",minus(n,m))
    
elif operator=='*':
    print("곱하기결과 : ",multiple(n,m))
elif operator=='/':
    print("실수 나눗셈 결과 : {:.2f}".format(division_a(n,m)))
elif operator=='//':
    print("정수 나눗셈결과 : ",division_b(n,m))
elif operator=='%':
    print("나머지결과 : ",division_c(n,m))

#(2)함수 이용X  (세부 사항은 귀찮아서 안씀 0으로 못나누고 이런거,걍 저렇게 식도 쓸수 있구나 하셈)
if operator=='+':
    print("뎃셈결과 : ",n+m)
elif operator=='-':
    print("뺄셈결과 : ",n-m)
    
elif operator=='*':
    print("곱하기결과 : ",n*m)
elif operator=='/':
    print("실수 나눗셈 결과 : ",n/m)
elif operator=='//':
    print("정수 나눗셈결과 : ",n//m)
elif operator=='%':
    print("뎃셈결과 : ",n+m)