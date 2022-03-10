def create_student(name, korean, math, english, science):
    return{
        "name" :name, 
        "korean": korean, 
        "math": math, 
        "english": english, 
        "science":science
        }

students = [
   create_student("윤인성", 87, 98, 88, 95),
   create_student("윤인성", 87, 98, 88, 95),
   create_student("윤인성", 87, 98, 88, 95),
   create_student("윤인성", 87, 98, 88, 95),
   create_student("윤인성", 87, 98, 88, 95)
]

# 학생을 한 명씩 반복
print("이름", "총점", "평균", sep = "\t")

for student in students:
    # 점수의 총합과 평균
    score_sum = student["korean"] + student["math"] + \
        student["english"] + student["science"]
    score_average = score_sum / 4
    # print
    print(student["name"], score_sum, score_average, sep="\t")
