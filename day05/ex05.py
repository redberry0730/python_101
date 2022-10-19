num = 10
'''
return 

1) 함수를 종료함
2) 프로그램의 흐름이 함수를 호출한 곳으로 돌아가게 함
    ㄴ return 값 이 있는 경우에는 값을 가지고 돌아감
    
'''
def add(n1, n2):
  print("덧셈")
  return n1 + n2
  print("덧셈")

result = add(11, 22)
print('result :',result)
print("-----------------")

def say_name(name):
  if name == "이순신":
    return
  print(f"{name}님, 안녕하세요")

say_name("강감찬")
say_name("이순신")
say_name("안중근")


'''
default argument - 맨 뒤의 parameter 에 설정함 
'''
def info_person(name, age, man=True):
  print(f"이름은 {name}입니다")
  print(f"나이는 {age}살입니다")
  if man:
    print("남자입니다")
  else:
    print("여자입니다")

info_person("더조은", 24)
info_person("더조은", 24, True)
info_person("아카데미", 21, False)


