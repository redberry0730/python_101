class GrandParent:
  def __init__(self):
    print("GrandParent")
class Parent1(GrandParent):
  def __init__(self):
    print("Parent1")
    super().__init__()
class Parent2(GrandParent):
  def __init__(self):
    print("Parent2")
    super().__init__()
class Child(Parent1, Parent2):
  def __init__(self):
    print("Child")
    super().__init__()
Child()