num=10
'''
readlines()
  ㄴ 파일의 모든 줄(행)을 읽어서
     각각의 줄(행)을 요소로 하는
     리스트를 반환함
'''
fl = open("D:/io_test/newfile1.txt", "rt", encoding="UTF-8")

while True:
  text_line = fl.readlines()
  if not text_line:
    break
  print(text_line)

fl.close()