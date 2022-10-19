
language1 = ["python", "java", "Go"]
language2 = ["C", "C#", "C++"]

language = language1 + language2
print(language)

list_numbers = [23, 1, 5, 63, 89, 3, 7, 10]

print("최댓값 :",max(list_numbers))
print("최솟값 :",min(list_numbers))
print("합 계 :",sum(list_numbers))
print("평 균 :",sum(list_numbers) / len(list_numbers))

import numpy as np
arr_numbers = np.array(list_numbers)
average = np.mean(arr_numbers)
print('평 균 :',average)

import statistics as st
average = st.mean(list_numbers)
print('평 균 :',average)

'''
 다음 list_nums 에서 짝수만 출력하세요
'''
list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_nums)
print(list_nums[:])
print(list_nums[::])
print(list_nums[::1])
print(list_nums[::2])
print(list_nums[1::2])

list_company = ['더조은', '네이버', '삼정전자', 'SK하이닉스']
'''
더조은 네이버 삼정전자 SK하이닉스
join() 사용
'''
print(" ".join(list_company))

'''
더조은 
네이버 
삼정전자 
SK하이닉스

'''
print("\n".join(list_company))

str_company = "더조은/삼성전자/SK하이닉스"
# ['더조은','삼성전자','SK하이닉스']
# split() 사용하기
print(str_company.split("/"))





