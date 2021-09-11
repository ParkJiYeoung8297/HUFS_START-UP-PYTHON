num=int(input("원화를 입력하세요: "))
a=str(num/1360)
b=str(num/1576)
c=str(num/1153)
d=str(num/10)
e=str(num/177)
print("1000원 은 "+a+ "유로 입니다")
print("1000원 은 "+b+ "파운드 입니다")
print("1000원 은 "+c+ "위안 입니다")
print("1000원 은 "+d+"유로 입니다")
print("1000원 은 "+e+"달러입니다")



#-----------------------------
number=int(input("연봉을 입력하세요: "))
print("연봉은 "+str(number)+" 원 입니다.")
a=number/12
b=a/4
print("월급은 "+str(a)+" 원 입니다.")
print("주급은 "+str(b)+" 원 입니다.")


#--------------------------------------
num=int(input("첫 번째 정수를 입력하세요: "))
number=int(input("두 번째 정수를 입력하세요: "))
a=num+number
b=num-number
c=num*number
d=num//number
e=num%number
f=num/number
print("덧셈결과: "+str(a))
print("뺄셈결과: "+str(b))
print("곱셈결과: "+str(c))
print("정수 나눗셈 몫: "+str(d)+" 정수 나눗셉 몫 "+str(e))
print("정수 나눗셈 결과: "+str(f))

#------------------------------
sentence=input("문장을 입력하세요: ")
sen=sentence.strip()
a=sen[0]
b=sen[-1]
print("문장은 "+a+" 로 시작 됩니다")
print("문장은 "+b+" 로 끝납니다")
print("문장은 "+str(sentence.count(''))+" 글자로 이루어져 있습니다")
print("소문자로 변환된 문장 : "+sentence.lower())
print("대문자로 변환된 문장 : "+sentence.upper())
print("오른쪽 공백이 제거된 문장 : "+sentence.rstrip())
print("왼쪽 공백이 제거된 문장 : "+sentence.lstrip())
print("공백이 제거된 문장 : "+sentence.strip())
print("단어가 바뀐 문장 : "+sentence.replace('START','JUMP'))