
list_movie = ['지구의 밤','라바','문어선생님','원더']

'''
'작은 아씨들'
'''
list_movie.append("작은 아씨들")
print(list_movie)

'''
'문어선생님'과 '원더' 사이에
'미니언즈' 를 추가하세요
'''
idx = list_movie.index('원더')
list_movie.insert(idx, '미니언즈')
print(list_movie)

'''
'라바'를 list_movie 에서 삭제하세요
'''
list_movie.remove('라바')
print(list_movie)

'''
'문어선생님'을 list_movie 에서 삭제하세요
'''
del list_movie[1]
print(list_movie)

'''
'원더'를 list_movie 에서 삭제하세요
del & index()
'''
del list_movie[list_movie.index('원더')]
print(list_movie)

'''
'원더' 가 list_movie 에 있는지 없는지 알아보기
'''
print('원더' in list_movie) # False
print('미니언즈' in list_movie) # True



