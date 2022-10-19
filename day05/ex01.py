num=10

'''
  함수 (function)
  
   프로그램 작성시 반복되는 부분을 한 뭉치로 묶어서
   어떤 입력값이 주어졌을 때 
   어떤 결과값을 돌려주는 식으로 작성하는 부분
                 반환해 주는 (return)
   code 의 재사용을 구현함 
   
  작성 형식
                    외부로부터 값(data)을 받는 부분
   def 함수이름(매개변수부):
     수행할 code (statement)... 
     수행할 code (statement)... 
     수행할 code (statement)...
     return 리턴값 
  
    ㄴ 매개변수나 리턴값을 없는 경우도 있음  
   parameter 
   매개변수 : 함수를 작성(정의)할 때 정해주는 부분
               ㄴ 함수 호출시 어떤 값을 넣어주는지 정해 줌
                      argument : (인자, 인잣값, 인수)
                  매개변수가 없는 경우에는
                  함수이름 옆 ( )  안을 비워둠
               
   리턴값   : 함수를 호출하면 함수의 body(몸통)부분에
              작성한 code 들이 실행되는데
              그 결과로 함수를 호출한 곳으로 
              되돌려주는 값   
              리턴값이 없는 경우에는 
              return 키워드만 작성하거나
              return 키워드를 생략함 
              리턴값이 있는 경우에는 
              return 키워드를 생략할 수 없음          
'''
# 함수의 정의부 (definition)
#  ㄴ 함수가 어떤 일을 하는지 설명하는 부분
def greeting():  # 함수의 선언부 (declaration) : 이름, 매개변수
  print("Hello ~~~")  # 함수의 몸통(구현부 : body) : 실행 code 가 작성된 부분

# 함수 호출부 (call:invoke(invocation))
# 이름(argument)
greeting()

def say_hello(input_hello):
  print(input_hello)
  return

say_hello("안녕하세요")
print("greeting 함수와 say_hello 함수가 실행되었음")

say_hello(3333)
print("say_hello 함수가 실행되었음")

def sum(n1, n2, n3):
  result = n1 + n2 + n3
  return result

return_value = sum(11, 22, 33)
print(return_value)
print("sum 함수가 실행되었음")

