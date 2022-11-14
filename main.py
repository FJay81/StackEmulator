class stackEm:
  def __init__(self):
    STACK = []
    self.stack = STACK
    pass
  def push(self,item):
    self.stack.insert(0,item)
    pass
  def pop(self):
    return self.stack.pop(0)
  def view(self):
    return self.stack