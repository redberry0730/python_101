# 내장 함수 - built-in function
numb = 10
'''
abs : absolute number
'''
print(abs(-100))
print("----------------------------")

'''
iterable type : list, tuple, str, range
all(iterable type)
 ㄴ iterable type 속에 있는 모든 요소가
    0이 아닌 경우 -> True 를 반환
    0이 하나라도 있는 경우 -> False 를 반환
'''
print(all([1, 2, 3, 4, 5]))
print(all([1, 2, 3, 4, 5, 0]))
print(all([1, 2, 3, 4, 0, 0]))
print(all([])) # 0 이 없으므로 True

print(bool([])) # 빈 list 이므로 False
print("----------------------------")

'''
iterable type : list, tuple, str, range
any(iterable type)
 ㄴ iterable type 속에 있는 모든 요소가
    모두 0인 경우 -> False 를 반환
    하나라도 0이 아닌 경우 -> True 를 반환
'''
print(any([1, 3, 5, 0, 3]))
print(any([0, 0, "", 0])) # False
print(any([])) # False
print("----------------------------")

'''
chr() : ASCII code 를 입력받아서
        해당 ASCII code 에 연결된 문자를 반환함
ord() : 입력받은 문자의 ASCII code 를 반환함        
'''
print(chr(65))
print(ord('A'))
print("----------------------------")
