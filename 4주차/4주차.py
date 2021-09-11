#리스트(array인듯)
month31=[1,3,5,7,8,10,12]
month30=[4,6,9,11]
week=['SUN','MON','TUE','WED','THU','FRI','SAT']
print(month31)#month31 인 array 가 그대로 출력됨
print(week)
print(month31[1:4])#1~4 위치에 있는 값들 출력(2번째에서 5번째 숫자 출력)
print(week[1])#이건 값이 하나이니까 [대괄호]없이 1위치에 있는 MON만 출력됨
print(week[-5:-2])#음수는 뒤부터 세는 것,작은 수가 앞에 있음 -5:-2

#리스트 함수
empty=[]#빈 리스트 생성 
#함수 쓰려면 먼저 빈 리스트라도 정의해줘야 하는듯, 이거 지우면 에러뜬다

#append():맨뒤에 값을 추가
empty.append('list')
empty.append(13)
empty.append('python')
print(empty)

#insert:원하는 위치에 삽입
empty.insert(1,'life')#1위치에 life를 넣어라(insert 해라),1위치에 life 들어가면서 원래 그 위치에 있던 것들이 뒤로 밀림

#extend:리스트끼리 합병
month31.extend(month30)#month31에 확장하여 month30 붙임
print(month31) #month31은 이제 합병된 month31 로 갱신 된거임

#pop:요소 삭제
empty.pop()#맨뒤 삭제
print(empty)
empty.pop(0)#0위치에 값 삭제
print(empty)

#remove:(요소)삭제
week.remove('WED')
print(week)

#clear:리스트 초기화(안에 요소들 전체 삭제)
empty.clear()
print(empty)

#변수이름.함수이름(요소or인덱스)
#sum,len
plus=month30[0]+month30[1]+month30[2]+month30[3]
plus2=sum(month30)
print(plus)
print(plus2)

print(len(week))#이건 array 길이 프린트하는 것

#
month=month30+month31 #두 리스트를 붙임
month_1=month30*4 #month30 리스트요소 4번 전체반복
print(month)
print(month_1)

