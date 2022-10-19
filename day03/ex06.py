
# 빈 딕셔너리 생성하기

dict_icecreams = {}
print(dict_icecreams)
print(type(dict_icecreams))
# <class 'dict'>
'''
icecream 이름 (key), price (value)

바밤바  1000
옥동자   700
메로나   800
'''
dict_icecreams = {'바밤바':1000, '옥동자':700, '메로나':800}

'''
부라보콘  1200
 쿠앤쿠    600
'''
print(dict_icecreams)

dict_icecreams['부라보콘']=1200
dict_icecreams['쿠앤쿠']=600

print(dict_icecreams)

'''
부라보콘의 가격을 출력하세요
'''
print('부라보콘 :',dict_icecreams['부라보콘'],'원')
'''
옥동자의 가격을 100원 인상해서 출력하세요
'''
print('옥동자 :',dict_icecreams['옥동자']+100,'원')
'''
쿠앤쿠를 딕셔너리 목록에서 삭제하세요
'''
del dict_icecreams['쿠앤쿠']
print(dict_icecreams)

dict_icecreams.pop('바밤바')
print(dict_icecreams)
print(dict_icecreams.pop('메로나')) # 800



