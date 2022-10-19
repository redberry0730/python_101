num = 10

'''
 set data type
   ㄴ index 번호가 없음 : Sequence type X 
             
 data 의 중복을 허용하지 않음
                  ㄴ data 를 구분할 수 있는 방법
                  
 순서가 없음 ( index 가 없기 때문에 )
                  
'''

list_nums  = [1, 2, 3, 2, 4, 1, 5, 8]
tuple_nums = (1, 2, 3, 2, 4, 1, 5, 8)

set_empty = {} # dictionary
print(type(set_empty)) # <class 'dict'>
set_empty2 = set() # <class 'set'>

print(type(set_empty2))

set_info = {"name":"이순신", "age":48, "height":48} # dictionary

set_numbers = {1, 2, 3, 4, 5}
print(set_numbers)
print(type(set_numbers))
set_nums = set([1, 2, 3])
print(set_nums)
print(type(set_nums))

set_str = set("python")
print(set_str)



set_empty = {} # dictionary
print(set_empty)

set_empty = set()
print(set_empty)


'''
 교집합, 합집한, 차집합
 대칭 차집합 : set1 ^ set2
'''

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

result = set1 & set2
print(result)

result = set1 | set2
print(result)

result = set1.intersection(set2)
print(result)

result = set1.union(set2)
print(result)

result = set1 - set2
print(result)

result = set2 - set1
print(result)

result = set1.difference(set2)
print(result)

result = set2.difference(set1)
print(result)


set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# (set1 - set2) U (set2 - set1)
# 대칭 차집합
result = set1 ^ set2
print(result)





