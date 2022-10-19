num=0
'''
List Comprehension
리스트 내포 : list 안에 for 문을 포함
'''

list_nums1 = [1, 2, 3, 4, 5]
list_nums2 = []  # [3, 6, 9, 12, 15]

for num in list_nums1:
  list_nums2.append(num * 3)

print(list_nums1)
print(list_nums2)

 # list_nums1 = [1, 2, 3, 4, 5]
list_nums3 = [num * 3 for num in list_nums1]
print(list_nums3)

'''
list_num1 의 요소(item)들을
제곱해서 list_num4 에 저장하세요
'''
list_num4 = [num * num for num in list_nums1]
print(list_num4)

'''
list_nums1 = [1, 2, 3, 4, 5]
list_num1 의 요소(item)들 중에서
짝수들만 list_nums5 에 저장하세요
'''
list_nums5 = []
for num in list_nums1:
  if num % 2 == 0:
    list_nums5.append(num)
print(list_nums5)  # [2, 4]

list_nums5 = [num for num in list_nums1 if num % 2 == 0]
print(list_nums5)  # [2, 4]

'''
2 단부터 4 단까지의 구구단을
리스트 내포 형식으로 작성하고
출력하세요 

list_gugu24 = [        ]
'''
for i in range(2, 5):
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")
  print()

list_gugu24 = [ i * j for i in range(2, 5) for j in range(1, 10)]
print(list_gugu24)