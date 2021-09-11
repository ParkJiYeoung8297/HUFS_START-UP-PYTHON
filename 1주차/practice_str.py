sentence=int(input("숫자를 입력하세요")) #문자형 변수를 int로 바꿔줌 so 문자 입력하면 int 로 바꿀수 없으므로 error 뜸
print(type(sentence)) #이건 sentence 의 타입을 출력함 즉 int 출력함

a=100
b=int(a)
c=float(a)
d=str(a)  #string 을 파이썬에서 str로 씀
print(type(a),type(b),type(c),type(d))


#:슬라이싱-첫번째 글자 마지막 글자 3~6번째 글자:#
sentence=input("문장을 입력해주세요:")
print(sentence)
print(sentence[0])#첫번째 글자 출력,이때 공백 인정
print(sentence[3]) #대괄호 안에 3은 3 위치에 있는 글자 출력
#이때 주의 할 점은 sentence첫번째 글자는 0번째 위체에 있음.0123이렇게 그래서 [3]이면 sentence의 4번째 글자가 나와야함
print(sentence[-1]) #음수는 뒤에서 부터임 뒤에서 첫번째 글자가 -1임,마지막 문자 출력
print(sentence[2:5])#이거는 2에서5위치에 있는 문자 출력 즉 sentence의 3~6번째 글자 출력


#:문자열 연산:#
print(sentence+sentence) #sentence랑 sentence붙여서 출력
print(sentence*3) #sentence 3번 출력하라
print(sentence,sentence) #sentence 출력 후 한칸 띄고 sentence 출력

word=sentence+sentence
word2=sentence*3
print(word)
print(word2)


#:문자열 관련 함수:#
print(sentence.count('u')) #u의 개수 세기
print(sentence.lstrip())  #left 공백 없애기
print(sentence.rstrip())  #right 공백 없애기
print(sentence.strip())   #양쪽의 공백 없애기
print(sentence.upper())  #전부 대문자로
print(sentence.lower())   #전부 소문자로
print(sentence.index('u'))  #u가 몇번째 syntex에 있니?(n번째 글자라면 n-1에 위치하는 거임)
print(sentence.replace('u','a')) #u를 전부 a로 바꿔줘