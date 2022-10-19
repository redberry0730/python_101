'''
dict_market 에 날짜를 키값으로 하는 OHLC 가 저장된 경우
dict_market 과 날짜(키값)를 입력받아서
OHLC 리스트를 반환하는 함수를 작성하세요
O : OPEN PRICE 시가
L : LOW PRICE 저가
H : HIGH PRICE 고가
C : CLOSE PRICE 종가
'''
dict_market = {"04/01" : [10300, 10100, 10500, 10200],
               "04/02" : [10100, 10000, 10500, 10300],
               "04/03" : [10100, 10000, 10700, 10500]}

def print_price(dictionary, date):
  return dict_market[date]

olhc = print_price(dict_market, "04/03")
print(olhc)
print("--------------------------------------------")

'''
문자열을 입력받아서
해당 문자열을 구성하는 각각의 문자들을
요소로 하는 리스트를 반환하는 함수를 작성하세요

 'python' --> ['p','y','t','h','o','n']
'''
def list_character(string):
  list_char = []
  for ch in string:
    list_char.append(ch)
  return list_char

result = list_character("python_programming")
print(result)
print("--------------------------------------------")

'''
아래의 (숫자모양의)문자열을 
정수로 반환하는 함수를 작성하세요
"34,567,281"  -->  34567281
'''

def string2int(string):
  string = string.replace(",", "")
  return int(string)

string_number = "34,567,281"
result = string2int(string_number)
print(result)
print("--------------------------------------------")

