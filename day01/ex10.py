
# str.format() 함수(메소드) 사용하기
fruit = "메론"
count = 3
days = 2
#           %s   %d
print('나는  {}을 {} 개 먹었습니다.'.format(fruit, count))

print('나는 {0}을 {1} 개 먹었습니다.'.format(fruit, count))
print('나는 {fruit}을 {count} 개 먹었습니다.'.format(fruit="귤", count=20))

print('나는 {1} 개의 {0}을 먹었습니다.'.format(fruit, count))
print('나는 {count} 개의 {fruit}을 먹었습니다.'.format(fruit="곶감", count=10))

print('나는 {number} 개의 {food}을 먹었습니다.'.format(food="곶감", number=10))
print('나는 {number} 개의 {0}을 먹었습니다.'.format("곶감", number=7))


print("나는 {2}일 동안 배가 아팠습니다. "
      "{1} 를 {0} 개 먹었기 때문입니다." \
      .format(count, fruit, days))

print("나는 {days}일 동안 배가 아팠습니다. "
      "{fruit} 를 {count} 개 먹었기 때문입니다." \
      .format(days=3, fruit="화채", count=4))

print("나는 {days}일 동안 배가 아팠습니다. "
      "{fruit} 를 {count} 개 먹었기 때문입니다." \
      .format(count=4, days=3, fruit="화채"))

# 왼쪽 정렬
# 0:<10 <-- 0 :인덱스번호, argument 의 인덱스번호
#           10: 문자열을 출력할 수 있는 자리수
print("{0:<10}".format("py"))
print("{:<10}".format("py"))
# 오른쪽 정렬
print("{0:>10}".format("py"))
# 가운데 정렬
print("{0:^10}".format("py"))

print("{0:<10}".format("py", "thon"))
print("{1:<10}".format("py", "thon"))

# 공백을 문자로 채우기
# 왼쪽 정렬
print("{0:=<10}".format("py"))
# 오른쪽 정렬
print("{0:=>10}".format("py"))
# 가운데 정렬
print("{0:=^10}".format("py"))

print("{0:*<10}".format("py"))
# 오른쪽 정렬
print("{0:*>10}".format("py"))
# 가운데 정렬
print("{0:*^10}".format("py"))
print("------------------------------")

# 숫자 출력하면서 정렬하기
figure = 3.1415926535
print("{0:0.4f}".format(figure))
print("{0:10.4f}".format(figure))
print("------------------------------")

str1 = "{0:0.4f}".format(figure)
#print(type(str1))
print(str1.rjust(10))
print(str1.ljust(10))

print("{{{0}}}".format("hello"))
print("{{{}}}".format("hello"))
# print("{{0}}".format("hello"))
# {0}

print(format(25689746, ','))

print("%15s" % format(25689746, ','))

print("{0:,}".format(25689746))

print("{0:>15,}".format(25689746))
print("{0:>20,}".format(25689746))