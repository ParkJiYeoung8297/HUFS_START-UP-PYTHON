name=input("이름을 입력하세요 : ")
subject1=input("과목1을 입력하세요 : ")
subject2=input("과목2를 입력하세요 : ")
subject3=input("과목3을 입력하세요 : ")

grade1=int(input(subject1+" 성적을 입력하세요 "))
grade2=int(input(subject2+" 성적을 입력하세요 "))
grade3=int(input(subject3+" 성적을 입력하세요 "))

if 90<=grade1 and grade1<=100:
    grade_1="A"
elif 80<=grade1:
    grade_1="B"
else:
    grade_1="C"

if 90<=grade2 and grade2<=100:
    grade_2="A"
elif 80<=grade2:
    grade_2="B"
else:
    grade_2="C"

if 90<=grade3 and grade3<=100:
    grade_3="A"
elif 80<=grade3:
    grade_3="B"
else:
    grade_3="C"



print("------------<성적표>-------------")
print("이름 :"+name)
print("{} 등급: {}".format(subject1,grade_1))
print("{} 등급: {}".format(subject2,grade_2))
print("{} 등급: {}".format(subject3,grade_3))
