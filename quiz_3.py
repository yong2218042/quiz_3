# 주어진 학생들의 점수
student_scores = [90, 45, 64, 9, 17, 29]

# 각 학생의 학점을 저장할 리스트
results = []

# 학생들의 점수를 학점으로 변환하고 결과 리스트에 추가
for score in student_scores:
    if score >= 71:
        grade = 'A'
    elif score >= 41:
        grade = 'B'
    elif score >= 11:
        grade = 'C'
    else:
        grade = 'D'

    results.append(grade)

# 최종 결과 출력
print(results)
