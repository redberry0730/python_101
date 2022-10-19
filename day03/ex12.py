
num = 20

'''
num 이 15 보다 크고 24 보다 작다면
'''
if num >= 15 and num <= 24:
  print("num 이 15 보다 크고 24 보다 작다")

if 15 <= num <= 24:
  print("num 이 15 보다 크고 24 보다 작다")

if True:
  print('a')
  print('b')
else:
  print('c')
print('d')

if True:
  if False:
    print('a')
    print('b')
  else:
    print('c')
else:
  print('d')
print('e')