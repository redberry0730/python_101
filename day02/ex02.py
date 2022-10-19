
# 마지작 네 자리 수만 출력하세요
license_number = "96가 9865"
print(license_number[4:])
print(license_number[-4:])

str1 = "홀짝홀짝홀짝홀짝"
print(str1[:])
print(len(str1))
print(str1[:8])
print(str1[0:8])

'''
str1[start:end:step(offset)]
step(offset) : 기본값 (1)
'''
print(str1[0:8:1])
print(str1[0:8:2])
print(str1[1:8:2])

str2 = "더조은아이티아카데미"
print(str2)
print(str2[:])
print(str2[::])
print(str2[::1])
print(str2[::3])
print(str2[::-1])

str3 = "python"
print(str3[:])
print(str3[::])
print(str3[::-1])

'''
 "-" 을 제거하고 출력하세요
 1) indexing + slicing
 2) replace
'''
phone = "010-6539-9867"
print(phone.replace("-",""))
print(phone.replace("-"," "))
print(phone[:2] + phone[4:8] + phone[9:])

'''
아래 url에서 naver만 출력하세요
 1) indexing + slicing
 2) split
'''
url = "https://www.naver.com"
print(url[12:17])
print(url.index("n"))
print(url[url.index("n"):url.index("n")+5])
print(url.split('.')[0])
print(url.split('.')[1])
print(url.split('.')[2])
print(url.split('.')[-1])