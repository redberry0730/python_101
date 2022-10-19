
#
tuple_movies = ('지구의 밤','라바','문어선생님')
print(type(tuple_movies))
list_movies = list(tuple_movies)
print(type(list_movies))
print(type(list(tuple_movies)))

m1, m2, m3  = tuple_movies
m1, m2, m3  = ('지구의 밤','라바','문어선생님')
m1, m2, m3  = '지구의 밤','라바','문어선생님'

num1 , num2 = 11, 22
num1 , num2 = (11, 22)

print(m1)
print(m2)
print(m3)

'''
range(end)
range(start, end)
range(start, end, step)
'''
range(10)
range(1, 10)
range(1, 10, 2)

print(range(10))
print(tuple(range(10)))
print(list(range(10)))

print(type(range(10)))

print(list(range(1, 11)))

print(list(range(1, 10, 2)))

list_odd = list(range(1, 11, 2))
print(list_odd)

list_even = list(range(0, 11, 2))
print(list_even)

list_nums = list(range(1, 11))
print(list_nums)

print('list_nums[1:] :',list_nums[1:])
print('list_nums[0:] :',list_nums[0:])
print('list_nums[:] :',list_nums[:])
print('list_nums[::2] :',list_nums[::2])  # odd
print('list_nums[1::2] :',list_nums[1::2])  # even

list_nums = [0,1,2,3,4,5,6,7,8,9,10]
print('list_nums[1:] :',list_nums[1:5])
print('list(range(1, 5)) :',list(range(1, 5)))
