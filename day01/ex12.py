
str1 = "hello python"
print("str1.count('o') :",str1.count('o'))
print("str1.count('l') :",str1.count('l'))

str2 = "python programming is the best programming language"
print("str2.find('b') :",str2.find('b'))
print("str2.find('z') :",str2.find('z')) # : -1 없는 문자

print("str2.index('b') :",str2.index('b'))
# print("str2.index('z') :",str2.index('z'))
# ValueError: substring not found

# "python programming is the best programming language"
print("str2.index('i') :",str2.index('i'))
print("str2.rindex('i') :",str2.rindex('i'))

print("str2.find('i') :",str2.find('i'))
print("str2.rfind('i') :",str2.rfind('i'))
print("---------------------------------")

str3 = "pyTHon progRAMming"
print('str3 :',str3)
print('str3.upper() :',str3.upper())
print('str3.lower() :',str3.lower())
print('str3.capitalize() :',str3.capitalize())
print('str3.title() :',str3.title())
print("---------------------------------")

# join()
print(",".join('python programming'))

print(' '.join(['orange','blue','red','yellow','white','pink']))

print('-'.join(['orange','blue','red','yellow','white','pink']))

print('|'.join(['orange','blue','red','yellow','white','pink']))


# split()

str4 = "Python is the best programming language"
print("str4.split() :",str4.split())

str5 = "orange|blue|red|yellow|white|pink"

print("str5.split(\"|\") :",str5.split("|"))

# replace()

str6 = "Python is the best programming language"
print(str6.replace("the best", "one of the"))


# strip(), rstrip(), lstrip()
str7 = " python "
print("str7.strip() :",str7.strip())
print("str7.rstrip() :",str7.rstrip())
print("str7.lstrip() :",str7.lstrip())





