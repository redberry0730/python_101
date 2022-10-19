fl = open("say_hello.txt", "rt", encoding="UTF-8")

line1, line2, line3 = fl

print(line1)
print(line2)
print(line3)

fl.close()

