
str1 = "python proqramming"
print(str1)
print(str1.replace("q", "g"))

'''
id() : 주소 반환
'''
print("id(str1)  :",id(str1))
print("id(str1)' :",id(str1.replace("q", "g")))

'''
 str type : immutable type VS mutable type
             불변형
'''

listing_stock = "9,658,542,357"
'''
',' 를 제거하고 숫자형으로 바꾸세요
'''
print(listing_stock.replace(",", ""))
result = listing_stock.replace(",", "")
int(listing_stock.replace(",", ""))
print(int(result))
print(int(result) + 10)

str2 = " py "
print(str2)
print(str2.strip())

'''
ljust(), rjust()
'''

str3 = "python"
'''
전체 문자열의 길이를 20으로 하고
'python' 을 왼쪽(오른쪽, 가운데)으로 정렬하기
'''
print(str3.ljust(20))
print(str3.rjust(20))
print(str3.center(20))


str4 = ",My private programming languages are python, java and CLang."
print(str4)
print(str4.strip(',.'))

str5 = ', python.'
print(str5.strip(',.'))

import string

str6 = ",My private programming languages are python, java and CLang."
print(str6.strip(string.punctuation))
print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

str7 = ', python.'
print(str7.strip(string.punctuation))
print(str7.strip(string.punctuation + ' '))
