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