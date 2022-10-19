
'''
 숫자나 문자열 앞을 0으로 채우기
 zfill() : zero fill
'''
print('845'.zfill(5))
print('84.75'.zfill(5))
print('84.75'.zfill(10))
print('python'.zfill(10))

'''
endswith(), startswith()
'''
report_file = "report.xlsx"
print(report_file.endswith('xlsx')) # True

'''
xlsx 또는 xls 로 끝나는 파일인지 확인하기
'''
print(report_file.endswith(('xlsx', 'xls'))) # True

report_file = "2021_report.xlsx"
'''
2021 로 시작하는 파일인지 확인하기
'''
print(report_file.startswith("2021")) # True



