#1-4반 학급 성적
students=[
    {"이름": '송강호', 'korean':97,"math":91,"english":96,"science":82},
    {"이름": '아이유', 'korean':95,"math":90,"english":92,"science":86},
    {"이름": '송중기', 'korean':100,"math":88,"english":94,"science":90},
    {"이름": '김태리', 'korean':93,"math":87,"english":98,"science":94},
    {"이름": '송강', 'korean':87,"math":82,"english":96,"science":98},
]

for student in students:
    print(student.get("이름"))

#클래스
class Student :
    def __init__(self,name,korean,math,english,science):#self 제외한 변수들이 입력받는거
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    
    #class 에 종속된 함수=메서드 임.    
    def get_sum(self): #메서드는 함수만 부를수 없고 student.getsum 처럼 class종속된 형태로 가져올수 있음              
        return self.korean+self.math+self.english+self.science
    
    def average(self):
        return "{:2f}".format(self.get_sum()/4)

students=[
    Student("송강호",97,98,95,90),
    Student("아이유",97,90,100,82),
    Student("송중기",95,93,95,89),
    Student("김태리",88,92,95,100),
    Student("송강",87,98,92,85),
]

for student in students:
    print(f"{student.name} 총점: {student.get_sum()} 평균: {student.average()}")
