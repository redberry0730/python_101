num = 10

'''
 tuple (튜플) : index 번호가 있음
                  ㄴ str, list, tuple
   list([ ]) 와 거의 비슷함 
     ㄴ mutable
   
   ( ) 를 사용함
   tuple 은 immutable
   item(요소) 가 하나인 tuple 을 만들 때
   ()안에 요소를 넣고 뒤에 ',' 를 붙여주어야 함   

'''
tp1 = ()
tp2 = (1,)
tp3 = (1, 2, 3, 4, 5)
tp4 = 1, 2, 3, 4, 5
tp5 = (1, 2, 3, (4, 5, 6))
tp6 = ('python', 'programming', 'best', 'language')
tp7 = ('python', 'programming', ('best', 'language'))
tp8 = (1, 2, 'abc', 'tjoeun', True, (1, 3, "korea"))

tp5 = (1, 2, 3, (4, 5, 6), 'python', 'best')
print(tp5[2])
print(tp5[3])
print(tp5[3][1])
print(tp5[3:])

tp5_1 = (11, 22, 33, 'abcdefg')
tp_result = tp5 + tp5_1
print(tp_result)

print(len(tp5))
print(len(tp5_1))

print(tp5 * 3)

tp9 = (1, 2, 3)
# del tp9[0]
# TypeError: 'tuple' object doesn't support item deletion
















