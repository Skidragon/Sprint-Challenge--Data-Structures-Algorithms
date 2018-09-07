class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):

    queue = []
    while self:
      cb(self.value)

      if self.right is not None:
        queue.append(self.right)
    
      self = self.left


    for index in range(len(queue) -1, -1, -1):
      queue[index].depth_first_for_each(cb)
            
  
    


  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

if __name__ == '__main__':
  bst = BinarySearchTree(5)
  bst.insert(2)
  bst.insert(3)
  bst.insert(7)
  bst.insert(9)
  arr = []
  bst.depth_first_for_each(lambda x: arr.append(x))
  print(arr)