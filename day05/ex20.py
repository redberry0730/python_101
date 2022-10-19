list_lines = ["안녕하세요\n", "더조은\n", "아카데미입니다\n"]

with open("say_hello.txt", "wt", encoding="UTF-8") as fl:
  fl.writelines(list_lines)