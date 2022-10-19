
# set 자료형에 값 하나 추가하기
# mutable
set1 = {1, 2, 3}
print(set1)
set1.add(4)
print(set1)

# 값 여러 개 추가하기

set1.update({4, 5, 6})
print(set1)

set1.update([7, 8, 9])
print(set1)

set1.remove(6)
print(set1)

set_range = set(range(1, 11))
print(set_range)

set_kor = set("더조은아이티아카데미")
print(set_kor)

list_nums = [1, 2, 3, [4, 5], [6, 7], (8, 9)]
print(list_nums)
tuple_nums = (1, 2, 3, [4, 5], [6, 7], (8, 9))
print(tuple_nums)

'''
TypeError: unhashable type: 'set'
set data type 속에 set data type  을 포함할 수 없음
set_nums = {1, 2, 3, {4, 5}, {6, 7}}
print(set_nums)

'''

set1 = {1, 2, 3}

list_nums = [1, 2, 3, 2, 3, 5, 1, 1]
result_set = set(list_nums)
print(list_nums)
print(result_set)

tuple_set = (1, 2, 3, 2, 3, 5, 1, 1)
result_set = set(tuple_set)
print(tuple_set)
print(result_set)

'''
frozenset <-- immutable set

'''
set1 = {1, 2, 3, 4}
frozen1 = frozenset(set1)
print(frozen1)

set1.discard(2)
print(set1)
set1.discard(2)
print(set1)

set1.remove(3)
print(set1)


'''
immutable set
AttributeError: 'frozenset' object has no attribute 'add'
frozen1.add(5)
print(frozen1)

AttributeError: 'frozenset' object has no attribute 'update'
frozen1.update({7,8,9})

AttributeError: 'frozenset' object has no attribute 'discard'
frozen1.discard(2)

AttributeError: 'frozenset' object has no attribute 'remove'
frozen1.remove(3)
'''


'''
Object 
  <-- class(member variable + member method(function))
                속성             메소드(기능)
            property
              (= attribute)  
                
'''

