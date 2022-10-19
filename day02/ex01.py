
# 문자열 인덱싱

str1 = "python program is the best programming language"
'''
 python program is the best programming language
012345678901234567890124567890124567890124567890
'''
print("str1[9]  :",str1[9])
print("str1[22] :",str1[22])
print("str1[-1] :",str1[-1])
print("str1[-2] :",str1[-2])
print("str1[-3] :",str1[-3])

print("str1[18]+str1[19]+str1[20] :",str1[18]+str1[19]+str1[20])

'''
slicing
'''
print("str1[18:20] :",str1[18:20])
print("str1[18:21] :",str1[18:21])

print("str1[0:6] :",str1[0:6])
print("str1[:6] :",str1[:6])
print("str1[:27] :",str1[:27])
print("str1[:38] :",str1[:38])
print("str1[:39] :",str1[:39])
print("str1[:-8] :",str1[:-8])
print("str1[:-9] :",str1[:-9])
print("str1[-20:-9] :",str1[-20:-9])


date_info = "20210425Sunny"

# 날짜 (연도-달-날짜)
print(date_info[0:8])
print(date_info[:8])
# 날씨
print(date_info[8:13])
print(date_info[8:])
# 연도
print(date_info[:4])
# 달
print(date_info[4:6])
# 날짜
print(date_info[6:8])


