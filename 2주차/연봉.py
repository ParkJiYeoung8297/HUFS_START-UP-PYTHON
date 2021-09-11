salary_y =int(input("연봉을 입력하세요: "))
salary_m = salary_y /12
salary_w = salary_m / 4

print('연봉은{:10.3f}원 입니다.'.format(salary_y))
print('월급은{:10.3f}원 입니다.'.format(salary_m))
print('주급은{:10.3f}원 입니다.'.format(salary_w))
