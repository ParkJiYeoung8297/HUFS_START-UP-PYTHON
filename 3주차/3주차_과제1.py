print("계산기 메뉴얼은 다음과 같습니다")
print("1: 사칙연산계산기 2: 환율계산기 3: 연봉계산기")
num=int(input("메뉴얼을 입력하세요 :"))

if num==1: #계산기
    manual=input("계산할 연산 기호를 입력하세요 :")
    num_1 =int(input("첫 번째 정수를 입력하세요(두자리 수 이하): "))
    num_2 =int(input("두 번째 정수를 입력하세요(두자리 수 이하): "))



    add_result = num_1 + num_2
    minus_result = num_1 - num_2
    mul_result = num_1 * num_2
    division_result_i = num_1 // num_2
    division_result_f = num_1 / num_2
    remain_result = num_1 % num_2

    if num_1<100 and num_2<100:

        if manual=="+":
            print("덧셈결과: ", add_result)
        elif manual=="-":
            if num_1>=num_2:
                print("뺄셈 결과: ", minus_result)
            else:
                print("숫자가 잘못되었습니다")
        elif manual=="*":
            print("곱셈 결과: ", mul_result)
        elif manual=="//":
            if num_2!=0:
                print("정수 나눗셈 몫:{:.1f}".format(division_result_i))
            else:
                print("0으로 나눌수 없습니다")
        elif manual=="%":
            if num_2!=0:
                print("정수 나눗셈 나머지:{:.1f}".format(remain_result))
            else:
                print("0으로 나눌수 없습니다")
        elif manual=="/":
            if num_2!=0:
                print("정수 나눗셈 결과:{:.1f}".format(division_result_f))
            else:
                print("0으로 나눌수 없습니다")
        else :
            print("올바른 연산이 아닙니다")
    else:
        print("두자리수가 아닙니다")


elif num==2: #환전
    nation=input("환전할 국가를 선택하세요 : ")
    won=float(input("원화를 입력하세요: "))
    ero=float(won/1360)
    found=float(won/1576)
    yuan=float(won/1153)
    yen=float(won/10)
    dollar=float(won/177)

    if nation=="유럽":
        print("{} 원 은 {:10.2f}  유로 입니다".format(won,ero))
    elif nation=="영국":
        print("{} 원 은 {:10.2f} 파운드 입니다".format(won,found))
    elif nation=="중국":
        print("{} 원 은 {:10.2f} 위안 입니다".format(won,yuan))
    elif nation=="일본":
        print("{} 원 은 {:10.2f}  유로 입니다".format(won,yen))
    elif nation=="미국":
        print("{} 원 은 {:10.2f}  달러입니다".format(won,dollar))
    else:
        print("해당 국가가 없습니다")

elif num==3: #연봉
    salary_y =int(input("연봉을 입력하세요: "))
    salary_m = salary_y /12
    salary_w = salary_m / 4

    print('연봉은{:10.3f}원 입니다.'.format(salary_y))
    print('월급은{:10.3f}원 입니다.'.format(salary_m))
    print('주급은{:10.3f}원 입니다.'.format(salary_w))

else:
    print("올바른 메뉴얼을 입력해주세요")