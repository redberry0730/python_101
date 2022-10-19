
# f-string 을 사용해서 문자열 출력하기

name="이순신"
job="장군님"

print(f"나의 이름은 {name}이고, 직업은 {job}입니다")

num1 = 10
num2 = 20

print(f"num1 + num2 = {num1 + num2} | num1 X num2 = {num1 * num2}")

print("num1 + num2 = %d | num1 X num2 = %d" % ((num1+num2), (num1*num2)))

print("num1 + num2 = {} | num1 X num2 = {}".format((num1+num2), (num1*num2)))

# tuple

data = ("안녕", 12345, "python")
print(f"data : {data}")
# %-formatting 방식은 str, int, float 만 지원함
# print("data : %s" % data)
print("data : %s" % str(data))

import datetime

now_date = datetime.datetime.now()
print(now_date)

print(f"{now_date:%Y-%m-%d} is on a {now_date:%A}")

print("{} is on a {}".format(now_date.strftime("%Y-%m-%d"), now_date.strftime("%A")))





