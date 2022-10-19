num = 10
'''

and  연산자
or   연산자

    True   and  True     :   True
    True   and  False    :   False
    False  and  True     :   False
    False  and  False    :   False
    
    True    or  True     :   True
    True    or  False    :   True
    False   or  True     :   True
    False   or  False    :   False
    
    값이 있으면  True    <--  1
    값이 없으면  False   <--  0
    
    None  <--  False
'''

str1 = None
str2 = 'A'

print('bool(None) :',bool(None))
result = str1 and str2
print('result :',result)
str1 = 11
result = str1 and str2
print('result :',result)
print("-------------------------")

str1 = None
result = str1 or str2
print('result :',result)

str1 = 11
result = str1 or str2
print('result :',result)
print("-------------------------")

str1 = 'C'
str2 = 111
result = str1 and str2
print('result :',result)
result = str1 or str2
print('result :',result)
print("-------------------------")

v1 = []
v2 = [1, 2, 3]
result = v1 and v2
print('result :',result)
result = v1 or v2
print('result :',result)
print("-------------------------")

v1 = [1, 2, 3, 4, 5]
v2 = ['a', 'b', 'c', 'd', 'e']
result = v1 and v2
print('result :',result)
result = v1 or v2
print('result :',result)
print("-------------------------")

print('a' and (3-1))
print(0 and (3-1))
print("-------------------------")

