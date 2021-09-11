name=[1,'John',2,'mike']
for xlie in name:
    print(xlie)


list=[1,2,3,4]
for ylie in list:
    ylie=ylie+1 #이거는 list 갱신 안됨
    print(ylie)
print(list)#최초 list 그대로 출력


for i in range(len(list)):#list 길이만큼만 반복한다는 뜻이지 즉 range(4)임
    list[i]=list[i]+1 #이거는 list 갱신됨
    print(list[i])
print(list)#갱신된 list 출력됨

print("엔터를 하고 싶지 않아!",end=' ')#end 이거 하면 enter(줄바꾸기) 안하고 출력
print("이야야야",end='!')