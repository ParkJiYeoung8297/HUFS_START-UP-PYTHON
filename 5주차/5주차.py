#input() 리스트 실습
name="park.ji.yeong"
print(name)
name=name.split('.')#괄호안에 있는 걸 기준으로 split(쪼갬)해서 리스트 저장하는 함수
print(name)         #[  ,   ,   ]이런 리스트 형식으로 출력됨

numbers=input().split()
print(numbers)

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])#numbers의 리스트가 모두 int로 형 변환 즉 출력될때'1'이었다면 형변환 후 1로 출력됨

print(numbers)

#tuple(자료의 생성 삭제 불가능,즉 요소를 새로운 값으로 갱신 불가)

tup=() #빈tuple도 가능
tup1=(1)
tup2=(1,2,3)
tup3=('apple','banana')
tup4=1,2,3,4  #tuple은 대괄호 없이도 리스트로 알아듣고 리스트로 출력함
tup5=(('ab','cd'),'ab','cd',True)

print(tup)
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)

print(tup4[1:])#인텍스 1 부터 끝까지
print(tup3[1])
print(tup3[-1])

#tup4[3]=7 이거 불가능 에러뜸 tuple은 값 갱신 불가니까
numbers[3]=8#리스트는 갱신 가능ㅋㅋㅋ
print(numbers)

#  +  *
plus_tup=tup3+tup2#두 tuple 을 붙임
#tup1+tup2로 하면 에러 뜸 왜냐하면 tup1의 자료형이 1 하나뿐이므로 이건 tup로 인식 하지않고 숫자 1 로써 인식함
#그래서 tup1+tup2하면 왜 숫자1이란 tup을 더하냐고 인식해서 에러가 뜸
multiple_tup=tup3*3#3번 반복

print(plus_tup)
print(multiple_tup)

#딕셔너리
dictionary_1={
    'apple':'사과',#쉼표,없으면 에러뜸
    'banana':'바나나',
    'orange':'오렌지',
    'watermelon':'수박'
}

print(dictionary_1)
print(dictionary_1['apple'])#키값이 apple인 값 사과 가 출력됨
#print(dictionary_1[9]) 없는 값이라 에러뜸

dictionary_2={
    '이름':'박지영', #앞에가 인덱스 값(앞에가 키값), 뒤에가 값
    '나이':'미상',
    '학과':'산업경영공학과',
    '수업':'파이썬'
}

#조건문
if '이름' in dictionary_2:
    print(dictionary_2['이름'])
if '집주소' in dictionary_2:#집주소 라는 키값이 존재하면 밑에 실행 but dictionary_2에 집주소 없으니까 실행x
    print(dictionary_2['이름'])
#get함수
print(dictionary_2.get('학과')) #학과를 key값으로 갇는 값 출력
print(dictionary_2.get('파이썬'))#파이썬이라는 키값은 없음(키값은 왼쪽에 있는 수업임)'수업='파이썬'',그래서 None 출력

keys=[]
value=[]
for key in dictionary_2:
    keys.append(key) #dictionary_2의 키 값들을 리스로 추가(append)
    print(dictionary_2[key])
    value.append(dictionary_2[key]) #dictionary_2의 키값에 대응하는 요소들을 리스트로 추가

print(value)
print(keys)

