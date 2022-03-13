# 학생 리스트 선언
students = [
    {"name" : "배준호", "korean" : 25, "math": 100, "english":100, "computer": 100}
]

# 학생을 한 명씩 반복 합니다.
print("이름", "총점", "평균", sep = "\t")
for student in students:
    # 점수의 총합과 평균 계산
    score_sum = student["korean"] + student["math"] + student["english"] + student["computer"]
    score_average = score_sum / 4
    # 출력
    print(student["name"], score_sum, score_average, sep = "\t")
    