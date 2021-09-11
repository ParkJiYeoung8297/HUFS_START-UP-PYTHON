# 성적 분류기 만들기
name = input("이름을 입력하세요 : ")

#과목수
num=int(input("과목수를 입력하세요 : "))
sub=[]
score=[]
grade=[]
for i in range(num):
    temp = input(f"과목{i+1}을 입력하세요 : ")
    sub.append(temp)
print(sub)

for i in range(num):
    temp=int(input(f"{sub[i]} 성적을 입력하세요 : "))
    score.append(temp)
print(score)

for i in range(num):
    if score[i] >= 90 :
        grade.append('A')
    elif score[i] > 80 and score[i] <90 :
        grade.append('B')
    elif score[i] >= 0 and score[i] <80:
        grade.append('C')
    else:
        print("잘못된 숫자를 입력하셨습니다.")

print("--------<성적표>--------")
print(f"이름: {name.upper()}")
for i in range(num):
    print(f"{sub[i]} 등급: {grade[i]}")
