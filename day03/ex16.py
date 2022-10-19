
dict_season_fruit \
  = {"봄":"딸기","여름":"수박","가을":"사과"}
season = input("좋아하는 계절을 입력하세요 : ")

'''
입력한 계절이 dict_season_fruit 에 있다면
그 입력한 계절에 해당하는 과일을 출력하고
입력한 계절이 dict_season_fruit 에 없다면
"좋아하는 계절이 dict_season_fruit 에 없습니다"
를 출력하세요
'''

if season in list(dict_season_fruit.keys()):
  if season == list(dict_season_fruit.keys())[0]:
    print(list(dict_season_fruit.values())[0])
  elif season == list(dict_season_fruit.keys())[1]:
    print(list(dict_season_fruit.values())[1])
  elif season == list(dict_season_fruit.keys())[2]:
    print(list(dict_season_fruit.values())[2])
else:
  print("좋아하는 계절이 dict_season_fruit 에 없습니다")
