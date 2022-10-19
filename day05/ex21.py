with open("say_hello.txt", "rt", encoding="UTF-8") as fl:
  line_result = None
  while line_result != '':
    line_result = fl.readline()
    print(line_result.strip('\n'))