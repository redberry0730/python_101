class GrandParent:
  def __init__(self):
    print("GrandParent")
class Parent1(GrandParent):
  def __init__(self):
    print("Parent1")
    GrandParent.__init__(self)
class Parent2(GrandParent):
  def __init__(self):
    print("Parent2")
    GrandParent.__init__(self)
class Child(Parent1, Parent2):
  def __init__(self):
    print("Child")
    Parent1.__init__(self)
    Parent2.__init__(self)
chd = Child()