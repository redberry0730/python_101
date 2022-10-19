score = 73
message = "";
if score >= 60:
  message = "success"
else:
  message = "failure"
print("message")
print('-------------------------------------------')
'''
 삼항 연산자 (Ternary Operator)
'''
# 1) if를 사용한 삼항연산자
score = 50
message = "success" if score >= 60 else "failure"
print(message)

'''
2) and 와 or 를 사용한 삼항연산자
'''
message = score >= 60 and "success" or "failure"
print(message)


num1 = 11
num2 = 22
# print('bool(num2) :',bool(num2))
      # 조건식
result = num2 and num1 + num2 or num2 - num1
print(result)






