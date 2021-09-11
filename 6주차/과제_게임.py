jay=input("Jay가 선택한 카드(1~9에서 5장): ").split()
emily=input("Emily가 선택한 카드(1~9에서 5장): ").split()
machine=input("기계가 선택한 카드(1~9에서 3장): ").split()
set_j=set(jay)
set_e=set(emily)
set_m=set(machine)

set_jm=set_j.intersection(set_m)
set_j=set_j-set_jm #집합의 연산처럼 마이너스도 되네

set_em=set_e.intersection(set_m)
set_e=set_e-set_em

if len(set_j)==len(set_e):
    print("무승부입니다!")
elif len(set_j)>len(set_e):
    print("Jay 대 Emily는 {}:{}로 Jay 승!".format(len(set_j),len(set_e)))
else:
    print("Emily 대 Jay는 {}:{}로 Emily 승!".format(len(set_e),len(set_j)))