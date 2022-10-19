
# list 에 item(요소) 추가하기

print("---append()-------------------------------")
list1 = [1, 2, 3, 4, 5]
print(list1)
list1.append(6)
print(list1)
list1.append(7)
print(list1)
print("----------------------------------")

list1.append([8, 9])
print(list1)
print("----------------------------------")

list = []
print(list)
list.append(1)
print(list)
list.append([2, 3])
print(list)
list.extend([4, 5, 6])
print(list)
print("----list, extend 는 list 끝에 item 추가---------")
print("----insert 는 중간(index 지정)에 item 추가---------")
print("----insert : 지정한 index 에 원래 있던 요소가 ---------")
print("----뒤로 밀려나고 새로 넣는 data 가 그 자리로 들어감 ---------")

list.insert(3, 111)
print(list)
print("----list 맨 처음에 insert하기---------")
list.insert(0, 222)
print(list)
print("----list 맨 뒤에 insert하기---------")
list.insert(-1, 777)
print(list)
print("----list 맨 뒤에 insert하기---------")
list.insert(8, 999)
print(list)
print("----list 맨 뒤에 insert하기---------")
list.insert(len(list), 888)
print(list)
print("----list 중간에 insert하기---------")

list2 = [11, 22, 33, 44, 55]
# [11, 22, 300, 33, 44, 55]
list2.insert(2, 300)
print(list2)
print("----list 중간에 여러 개 insert하기 (덮어쓰기)---------")
# [11, 22, 300, 555, 777, 33, 44, 55]
list2[3:4] = [555, 777]
print(list2)  # [11, 22, 300, 555, 777, 44, 55]
print("----list 중간에 여러 개 insert하기 (덮어쓰지 않기)---------")
list2[5:5] = [123, 567]
print(list2)
# [11, 22, 300, 555, 777, 123, 567, 44, 55]

