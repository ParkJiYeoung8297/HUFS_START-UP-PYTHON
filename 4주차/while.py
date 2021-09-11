#1~10

count=1
result=0

while count<=10:
    result=result+count
    print(result)
    count=count+1
    print(count)
    print("-----")
print(f"합계{result}")#while문 마친 result 값 출력


# 만능계산기 프로그램
while True:#true 인동안 계속 반복 실행
    print("계산기 메뉴얼은 다음과 같습니다")
    print("1: 사칙연산 계산기 2: 환율 계산기 3: 연봉계산기 4:종료")
    m_calculator = int(input("메뉴얼을 입력하세요: "))
    if m_calculator == 1: # 사칙연산계산기를
        manual = input("계산할 연산기호를 입력해주세요: ")
        num_1 =int(input("첫 번째 정수를 입력하세요(두자리수 이하): "))
        num_2 =int(input("두 번째 정수를 입력하세요(두자리수 이하): "))

        if num_1 < 100 and num_2 < 100 :
            if manual == '+':
                add_result = num_1 + num_2
                print("덧셈결과: ", add_result)
            elif manual == '-':
                if num_1 >= num_2 :
                    minus_result = num_1 - num_2
                    print("뺄셈 결과: ", minus_result)
                else :
                    print("숫자가 잘못되었습니다.")
            elif manual == '*':
                mul_result = num_1 * num_2
                print("곱셈 결과: ", mul_result)
            elif manual == '/':
                if num_2 != 0:
                    division_result_f = num_1 / num_2
                    print("실수 나눗셈 결과: {:.1f}".format(division_result_f))
                else :
                    print("0으로 나눌 수 없습니다.")
            elif manual == '//':
                if num_2 != 0:
                    division_result_i= num_1 // num_2
                    print("정수 나눗셈 몫: ", division_result_i)
                else :
                    print("0으로 나눌 수 없습니다.")
            elif manual =='%':
                if num_2 != 0:
                    remain_result = num_1 % num_2
                    print("정수 나눗셈 나머지:", remain_result)
                else :
                    print("0으로 나눌 수 없습니다.")
            else :
                print("올바른 연산이 아닙니다~")

        else :
            print("두자리수가 아닙니다.")
    elif  m_calculator == 2 : # 환율계산기
        # 환율 계산기 과제
        # 원화를 입력 받음
        nation =input("환전할 국가를 선택하세요: ")
        won = int(input("원화를 입력하세요: "))
        # 국가별 환율 계산
        if nation == '유럽':
            euro = won / 1360
            print("{:8d}원은{:10.2f}유로입니다".format(won, euro))
        elif nation =='영국':
            pound = won /1576
            print("{:8d}원은{:10.2f}파운드입니다".format(won, pound))
        elif nation =='중국':
            yuan = won / 177
            print("{:8d}원은{:10.2f}위안입니다".format(won, yuan))
        elif nation =='일본':
            yen = won / 10
            print("{:8d}원은{:10.2f}엔입니다".format(won, yen))
        elif nation =='미국':
            dollar = won / 1153
            print("{:8d}원은{:10.2f}달러입니다".format(won, dollar))
        else:
            print("국가에대한 정보가 없습니다.")

    elif  m_calculator == 3: # 연봉계산기
        # 연봉 계산기 과제
        # 연봉을 입력 받음
        salary_y =int(input("연봉을 입력하세요: "))

        # 월급 계산
        salary_m = salary_y /12
        salary_w = salary_m / 4

        # 출력
        print('연봉은{:10.3f}원 입니다.'.format(salary_y))
        print('월급은{:10.3f}원 입니다.'.format(salary_m))
        print('주급은{:10.3f}원 입니다.'.format(salary_w))
    elif m_calculator==4:
        break# while,break 반복문에서 빠져나가기
    else :
        print("올바른 메뉴얼을 입력해 주세요")
