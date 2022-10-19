
# python 의 여러 문자열 출력 방법

'''
%-formatting
ㄴ format specifier
         ㄴ 서식문자, 형식문자, 변환문자, 양식문자
str.format()

f-string
'''
'''
%- formatting
'''
name = "이순신"
age = 48
print("이름 : " + name + ", 나이 : " + str(age))
print("이름 :",name,", 나이 :",str(age))
print("이름 : %s" % name)
print("나이 : %d" % age)
print("이름 : %s, 나이 : %d" % (name, age))

print("=" * 40)

# str.format()
print("이름 : {}, 나이 : {}".format(name, age))
print("=" * 40)

# f-string
print(f"이름 : {name}, 나이 : {age}")


'''
서식문자
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)

 literal data
 10 20 "더조은"
'''












