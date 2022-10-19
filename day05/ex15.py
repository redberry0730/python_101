num=10
'''
파일 생성하기

fl = open("파일이름.확장자", "파일열기모드", encoding속성="속성값")

파일열기모드 : 
 r  : read  - 읽기모드 
 w  : write - 쓰기모드
 rt : read  - text 형식으로 읽기모드 
 wt : write - text 형식으로 쓰기모드
 a  : (append) - 파일의 마지막 부분에 내용을 추가함
'''
#  I/O - Input, Output (입출력)
fl = open("D:/io_test/newfile1.txt", "wt", encoding="UTF-8")

for idx in range(1, 11):
  data = f"{idx} 번째 줄입니다\n"
  fl.write(data)

fl.close()












