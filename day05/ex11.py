list_numbers = list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_result \
  = list(map(lambda n : str(n) if n == 1 \
    else float(n) if n == 2 else n + 10, list_numbers))

print('list_result :',list_result)
'''
list_result : ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
'''


list_num1 = [1, 2, 3, 4, 5]
list_num2 = [6, 7, 8, 9, 10]


list_result = list(map(lambda n1, n2 : n1 * n2, list_num1, list_num2))
print('list_result :',list_result)
# list_result : [6, 14, 24, 36, 50]

