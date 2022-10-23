import array
class StackusingArray:
  def __init__(self):
    self.top=-1
    self.stack = array.array('i',[])
  def insert(self):
    self.element = int(input("Enter element to be insert:\n"))
    self.stack.append(self.element)
    self.top += 1
  def remove(self):
    if self.top==-1:
      print("stack empty")
    else:
      self.stack.pop()
      self.top -= 1
  def displaystack(self):
    if self.top==-1:
      print("stack empty")
    else:
      for i in self.stack:
        print(i)

      
r = StackusingArray()
print("Stack using array:\n 1.Push\n 2.Pop\n 3.Display\n 4.Exit\n")
while(True):
  chce = int(input("Enter Choice: "))
  if chce == 1:
    r.insert()
  elif chce == 2:
    r.remove()
  elif chce == 3:
    r.displaystack()
  else:
    print("LOL")
    break
