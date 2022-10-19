
fl = open("D:/io_test/newfile1.txt", "a", encoding="UTF-8")

for idx in range(21, 31):
  data = f"{idx} 번째 줄(행)입니다\n"
  fl.write(data)
fl.close()

