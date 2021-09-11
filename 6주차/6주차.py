list_a=[1,2,3,4,5,6,7,8,9,3,3,4,5,9,9,0]
#이때 list는 지정된 명령어이기 떄문에 if,for 처럼 변수이름으로 선언 하면 안됨
tuple_a=3,5,7,9
dictionary_a={
    '학생':'박지영',
    '보조강사':'김시은',
    '강사':'정태두'
    }

#int(input())
#자료형(변수)
list_b=tuple(list_a)#list_b 는 list_a를 tuple 로 형변환 한것
print(list_a)
print(list_b)
list_c=list(tuple_a)
print(tuple_a)
print(list_c)
list_d=list(dictionary_a)
print(dictionary_a)
print(list_d)

#set  집합(집합을 쓰면 합,차,교 집합등의 집합연산이 가능해짐)
set_a=set(list_a)
print(list_a)
print(set_a)
name_a=set("Hello HUFS! Welcome")
print(name_a)

#교집합(3,4,5) 합집합(1,2,3,4,5,6,7),차집합(1,2),(6,7)
set_b=set([1,2,3,4,5])
set_c=set([3,4,5,6,7])
print(set_b-set_c)
print(set_b&set_c)
print(set_b|set_c)

print(set_b.difference(set_c))#차집합
print(set_b.intersection(set_c))#교집합
print(set_b.union(set_c))#합집합

list_d=list(set_b)