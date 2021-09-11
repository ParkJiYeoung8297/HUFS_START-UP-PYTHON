name=input("이름을 입력하세요 : ")
num=int(input("입력할 과목의 갯수를 입력하세요 : "))
list_s=[]#리스트 정의 ,for 문 안에 쓰면 게속 빈리스트로 초기화 되니까 밖에서 정의 해주기
list_g=[]
for i in range (num): #i는 0부터 시작
    subject=input("과목{}을 입력하세요 :".format(i+1))
    grade=input(subject+"의 성적을 입력하세요 : ")
    grade_2=int(input(subject+"의 학점을 입력하세요 : "))
    list_s.append(subject)
    list_g.append(grade)
    total=0#초기화 필요함,이거 안쓰면 undefined 에러 뜬닫
    total=total+grade_2

print("------<성적표>-------")
print("이름 : "+name)
for i in range(num):
    print(list_s[i]+" 평점: "+list_g[i])
print("평점 : {:.2f}".format(total/num))