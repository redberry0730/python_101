'''
문자열 받아서 한 줄에 6 글자씩 출력하는
함수를 작성하고 호출하세요
'''
str_alphabet = "abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+|"

def print_6str(input_str):
  line = int((len(str_alphabet) / 6)) + 1
  for one_line in range(line):
    print(input_str[one_line * 6 : one_line * 6 + 6])

print_6str(str_alphabet)
print("--------------------------------------------")
'''
위의 함수를 
문자열과 한 줄에 출력할 글자 수 
두 개의 매개변수(parameter)를 갖는
함수로 변형해서 작성하고
호출해서 결과를 확인해 보세요 
'''
def print_6str2(input_str, characters):
  line = int((len(str_alphabet) / characters)) + 1
  for one_line in range(line):
    print(input_str[one_line * characters : one_line * characters + characters])

print_6str2(str_alphabet,4)
print("--------------------------------------------")


print_6str2(str_alphabet,3)
print("--------------------------------------------")

'''
연봉을 입력받아서 <-- parameter
월급을 반환하는 함수를 작성하고
호출하여 결과를 확인하세요
'''

def return_salary(annual_income):
  salary = annual_income / 12
  return salary

monthly_income = return_salary(70000000)
print("월급 : %.2f 원" % monthly_income)
print("월급 : %d 원" % monthly_income)
print("--------------------------------------------")






