num = 10
'''
이름    가격   재고
메로나  800     32
바밤바  700     15
옥동자  900      6
'''
dict_ice = {
            '이름':["메로나","바밤바","옥동자"],
            '가격':[800,700,900],
            '재고':[32, 15, 6]
          }
print(dict_ice)
'''
옥동자의 가격을 출력하세요
'''
print('옥동자 :',dict_ice['가격'][2],'원')
'''
바밤바의 재고량을 출력하세요
'''
print('바밤바 :',dict_ice['재고'][1],'개')
'''
투게더  10000 20
를 추가하세요
'''
dict_ice['이름'].append('투게더')
dict_ice['가격'].append(10000)
dict_ice['재고'].append(20)

print(dict_ice)

'''
이름    가격   재고
메로나  800     32
바밤바  700     15
옥동자  900      6
투게더 10000    20

아이스크림의 이름 : key
'메로나', '바밤바', '옥동자', '투게더'
[단가(가격), 재고] : value 
 '메로나' : [800, 32]
'''
dict_ice2 = {
              '메로나' : [800, 32],
              '바밤바' : [700, 15],
              '옥동자' : [900, 6],
              '투게더' : [1000, 20]
            }
print(dict_ice2)
'''
옥동자의 가격을 출력하세요
'''
print('옥동자 :',dict_ice2['옥동자'][0],'원')
'''
바밤바의 재고량을 출력하세요
'''
print('바밤바 :',dict_ice2['바밤바'][1],'개')
'''`
수박바 500  26
'''
dict_ice2['수박바'] = [500, 26]
print(dict_ice2)

'''
dict_ice2 
{'메로나': [800, 32], '바밤바': [700, 15], 
 '옥동자': [900, 6], '투게더': [1000, 20], 
 '수박바': [500, 26]}

아이스크림 이름으로 이루어진 리스트를 
생성하고 출력하세요
'''
list_names = list(dict_ice2.keys())
print(list_names)

'''
dictionary 에 있는 아이스크림
전체의 가격을 출력하세요
'''
# 1) + 연산
total = dict_ice2['메로나'][0] + dict_ice2['바밤바'][0] \
      + dict_ice2['옥동자'][0] + dict_ice2['투게더'][0] \
      + dict_ice2['수박바'][0];
print('합계 ',total,'원')

# 2) sum() 사용하기
list_values = list(dict_ice2.values())
# print(list_values)

sum = 0
for status in list_values:
  sum += status[0]
print('합계 ',sum,'원')
