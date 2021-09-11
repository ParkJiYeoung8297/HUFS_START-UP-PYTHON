nation=input("환전할 국가를 선택하세요 : ")
won=int(input("원화를 입력하세요: "))
ero=int(won/1360)
found=int(won/1576)
yuan=int(won/1153)
yen=int(won/10)
dollar=int(won/177)

if nation=="유럽":
    print("{} 원 은 {:10.2f}  유로 입니다".format(won,ero))
elif nation=="영국":
    print("{} 원 은 {:10.2f} 파운드 입니다".format(won,found))
elif nation=="중국":
    print("{} 원 은 {:10.2f} 위안 입니다".format(won,yuan))
elif nation=="일본":
    print("{} 원 은 {:10.2f}  유로 입니다".format(won,yen))
elif nation=="미국":
    print("{} 원 은 {:10.2f}  달러입니다".format(won,dollar))
else:
    print("해당 국가가 없습니다")
