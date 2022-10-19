
# 서식 지정자(format specifier) 사용하기

print("나의 이름은 %s 입니다" % "더조은")

name = "아카데미"
print("나의 이름은 %s 입니다" % name)

age = 24
print("나는 %d 살입니다" % age)

food = "감자"
number = 5
str1 = "나는 %s 를 %d 개 먹었습니다" % (food, number)
print(str1)

print("사과 %d 개가 있습니다" % 3)

total = 100
male = 60
female = 40

print("우리 반 학생들은 모두 %d 명이고 "
      "남자는 %d 명입니다. "
      "여학생의 비율은 %f%% 입니다"
      %(total, male, female))

print("우리 반 학생들은 모두 %d 명이고 "
      "남자는 %d 명입니다. "
      "여학생의 비율은 %.2f%% 입니다"
      %(total, male, female))

print("%s" % "py")
print("%10s" % "py")
print("%-10s" % "py")
print("%-10s더조은" % "hello")

print("%f" % 3.1415928272)
print("%.4f" % 3.1415928272)
print("%10.4f" % 3.1415928272)






