def currency(won,nation):#def 는 함수키워드,plus는 함수,won/nation은 매개변수
    if nation == '유럽':
            euro = won / 1360
            print("{:8d}원은{:10.2f}유로입니다".format(won, euro))
    elif nation =='영국':
            pound = won /1576
            print("{:8d}원은{:10.2f}파운드입니다".format(won, pound))
    elif nation =='중국':
            yuan = won / 177
            print("{:8d}원은{:10.2f}위안입니다".format(won, yuan))
    elif nation =='일본':
            yen = won / 10
            print("{:8d}원은{:10.2f}엔입니다".format(won, yen))
    elif nation =='미국':
            dollar = won / 1153
            print("{:8d}원은{:10.2f}달러입니다".format(won, dollar))
    else:
            print("국가에대한 정보가 없습니다.")


n=int(input("원화를 입력하세요: ")) #won,nation을 변수로 써도 상관없음,매개변수랑 이름 겨치던말던 둘이는 독립사건처럼 별개임
m=input("국가를 입력하세요: ")

currency(n,m)