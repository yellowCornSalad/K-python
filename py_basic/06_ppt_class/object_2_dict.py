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
def get_sum(students):
    score_sum = student["korean"] + student["math"] +  student["english"] + student["science"]
    return score_sum

    # 학생을 한 명씩 반복
def get_avg(student):
    return get_sum(student) / (len(student) -1)

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], get_sum(student), get_avg(student))
print("이름", "총점", "평균", sep = "\t")
    # print
for student in students:
    print(student_to_string(student))