
dict_ice = {'바밤바':1000, '옥동자':900, '메로나':700, '부라보콘':1200}
dict_ice2 = {'폴라포':500, '월드콘':1000}
print(dict_ice)
print(dict_ice2)
dict_ice['쭈쭈바']=600
print(dict_ice)
dict_ice.update(dict_ice2)
print(dict_ice)

list_fruits = ('banana','strawberry','grape','mango')
price = (3000,5000,8000,10000)
'''
key - list_fruits, value - price
'''
dict_fruits = dict(zip(list_fruits, price))
print(dict_fruits)

list_date = ['05/01','05/02','05/03','05/04']
close_price = [10100,10500,10300,10400]

dict_stocks = dict(zip(list_date, close_price))
print(dict_stocks)

dict_nums = {'a':10,'b':20,'c':30,'d':40}
print(dict_nums)

'''
setdefault(key)
setdefault(key, value)
추가만 되고, 수정은 안 됨
'''
dict_nums.setdefault('e')
print('dict_nums :',dict_nums)
dict_nums.setdefault('f', 50)
print('dict_nums :',dict_nums)
dict_nums.setdefault('f', 55)
print('dict_nums :',dict_nums)

print('---------------------------------------')

dict_nums['c'] = 33
print('dict_nums :',dict_nums)

'''
update(키key=값value) : key 가 문자열일 때만 가능함
'''
dict_nums.update(b=22)
print(dict_nums)

dict_nums.update(g=55)
print(dict_nums)

dict_nums.update(a=11, h=77)
print(dict_nums)

'''
update(키key=값value) : key 가 문자열일 때만 가능함
                        key 가 숫자인 경우
                         ㄴ update(딕셔너리형식)
'''
dict_height = {1:178, 2:185, 3:190}
print(dict_height)
dict_height.update({1:111})
print(dict_height)
dict_height.update({2:171, 4:185})
print(dict_height)

# {1: 111, 2: 171, 3: 190, 4: 185}
dict_height.update([[2, 181],[5, 175]])
print(dict_height)
dict_height.update([(1, 222),(6, 179)])
print(dict_height)
dict_height.update(((2, 192),(7, 188)))
print(dict_height)

# {1: 222, 2: 192, 3: 190, 4: 185, 5: 175, 6: 179, 7: 188}
dict_height.update(dict(zip([1, 2],[333, 555])))
print(dict_height)

dict_height.update(zip([1, 2],[300, 500]))
print(dict_height)