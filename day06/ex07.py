num = 10
'''
 클래스 : data 를 메모리에 loading 시킬 때
          어떤 구성(모양)으로 loading 할지를
          설명해 놓은 소스 - 설계도
          
          클래스 = 멤버번수 + 멤버메소드
          
          Object = 속성        +   기능
                   property        method
                   status(상태)  
          
 객체(Object, instance)
        : 클래스에 설명해 놓은대로 
          메모리에 loading 되어서 
          활성화된 상태의 data - 실체
'''

number = 111

def add(n1, n2):
  return n1 + n2

add(11, 22)

class Person:
  def say_hello(self):
    print("안녕하세요")

p1 = Person()
print(id(p1)) # 2498396803760
p1.say_hello()

p2 = Person()
print(id(p1))
p3 = Person()
print(id(p1))
p4 = Person()
print(id(p1))
p5 = Person()
print(id(p1))

p2.say_hello()
p3.say_hello()
p4.say_hello()
p5.say_hello()

print("----------------------------------")


