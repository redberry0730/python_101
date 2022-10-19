num=10
'''
입력된 문자열을 거꾸로 출력하는
함수를 작성하고 호출하세요
(결과를 출력하세요)
[힌트] 슬라이싱
'''
def reverse_str(str):
  return str[::-1]

print(reverse_str("python"))
print("----------------------------------")

'''
3 명의 학생 성적이 저장된 성적 리스트가 있습니다.
학생들의 성적을 입력받아서
평균을 반환하는 함수를 작성하고 호출하세요 
'''
list_scores = [99, 76, 85]

def calc_average(list_scores):
  total  = 0
  for score in list_scores:
    total += score
  average = total / len(list_scores)
  return average

print('평균 :',calc_average(list_scores), '점')
print('평균 : %.2f 점 ' % calc_average(list_scores))
print("----------------------------------")

'''
숫자들이 저장된 리스트를 입력받아서
짝수만 반환하는 함수를 작성하고 호출하세요(출력)
'''
list_numbers = [1, 5, 3, 8, 9, 2, 5, 4, 10]
def even_numbers(list_numbers):
  list_evens = []
  for number in list_numbers:
    if number % 2 == 0:
      list_evens.append(number)
  return list_evens
print(even_numbers(list_numbers))
print("----------------------------------")
'''
학생 한 사람의 정보(이름, 나이, 성별)가 저장된
dictionary 를 입력받아서
dictionary 의 key값만 반환하는 함수를 작성하고
호출하세요
'''
dict_info = {"이름":"더조은","나이":32,"성별":"남"}
def return_keys(dictionary):
  list_keys = []
  for key in dictionary.keys():
    list_keys.append(key)
  return list_keys
print(return_keys(dict_info))

print("----------------------------------")
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











