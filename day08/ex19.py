def outerfunct():
  n1 = 3
  n2 = 5
  def innefunc(n3):
    return n1 * n2 + n3
  # 내부 함수를 return 해 줌
  return innefunc

# result 에 내부함수가 할당됨
result = outerfunct()
print(result)
print(result(2))

print(outerfunct()(3))