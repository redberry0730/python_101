
def say_hello():
  print("hello")
say_hello()
print("---------------------------")

print("A")
def message():
  print("B")
print("C")
message()
print("---------------------------")


print("A")
def message1():
  print("B")
print("C")
def message2():
  print("D")

message1()
print("E")
message2()
print("---------------------------")


def message1():
  print("A")
def message2():
  print("B")
  message1()
message2()
print("---------------------------")

def message1():
  print("A")
def message2():
  print("B")
def message3():
  for idx in range(3):
    message2()
    print("C")
  message1()
message3()
