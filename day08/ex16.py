n = 22
print(n)

def test():
  global n
  n = 11
  # print(n)

test()
print(n)

