students = [
    { "name" :"윤인성", "korean": 87, "math": 98, "english": 88, "science":95},
    { "name":"홍길동", "korean": 90, "math": 98, "english": 88, "science":95},
    { "name": "김길동", "korean": 37, "math": 98, "english": 88, "science":95},
    { "name": "오길동", "korean": 81, "math": 98, "english": 88, "science":95},
    { "name": "정길동", "korean": 84, "math": 98, "english": 88, "science":95},
    { "name": "고길동", "korean": 81, "math": 98, "english": 88, "science":95}
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
