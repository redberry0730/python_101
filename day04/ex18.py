
answer   = [1, 3, 4, 2, 2]
solution = [1, 2, 4, 1, 2]

# 전체 문항수
count_problem = len(solution)

# 학생이 입력한 답안이 정답지와 일치한 경우
correct = 0
# 정답률 : 학생이 입력한 답안이 정답지와 일치한 비율
correct_rate = 0

# correct_rate = correct * (100 / count_problem)

for i in range(count_problem):
  correct = int(answer[i] == solution[i]) # True 이면 맞힌 문제
  correct_rate += correct * (100 / count_problem)
                             # 20
print(f"정답률은 {correct_rate}%입니다")
