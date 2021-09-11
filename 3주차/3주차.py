# 연봉 계산기 과제
# 연봉을 입력 받음
salary_y =int(input("연봉을 입력하세요: "))

# 월급 계산
salary_m = salary_y /12
salary_w = salary_m / 4

# 출력
print('연봉은', salary_y,'원 입니다.')
print('월급은', salary_m,'원 입니다.')
print('주급은', salary_w,'원 입니다.')

word='{}{}'.format(10,20) #챂에 넣은 형식대로 출력됨,so 앞에 중괄호 개수랑 뒤에 변수 개수가 같아야함.
#''안에 쓴 형식 그대로 나오는거라 '{}   {}'이렇게 띄어쓰기 넣으면 반영됨
print(word)

#위에 출력을 저 형식으로 쓰면
print('연봉은{:10.2f}원 입니다.'.format(salary_y)) #10.2f에서 10은소수점 자리 포함한 총 10자리수이다.이고 2f는 소수점 자리수 즉 두번째 자리 까지
#자리수 맞춰서 7자리 적히면 남은 자리는 공백으로 채움
print('월급은{:10.2f}원 입니다.'.format(salary_m))
print('주급은{:10.2f}원 입니다.'.format(salary_w))

#boolen 형식 true false
print(5>3)
print(5<3)
print(3==3)
print(4!=3)
print(4<=8)
print(7>=8)


#if
x=float(input("학점을 입력하세요 :"))

if x==4.5:
    print("신")
#사실 else이기 때문에 4.5 미만은 안써도 되긴한데 다른 프로그래밍 언어에서는 오류 날수있으니 걍 쓰는 연습(파이썬은 오류 잘 안남)
elif 4.2<=x and x<4.5: #elif 는 else if 임
    print("교수님의 사랑")
elif 3.5<=x and x<4.2:
    print("현 체제의 수호자")
else :
    print("분발해주세요")
#드래그 해서 tab누르면 전체가 다 들여쓰기 됨.