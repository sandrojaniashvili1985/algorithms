class Hashtable:
  def __init__(self):
    self.size = 10
    self.keys = [None] * self.size
    self.value = [None] * self.size

#A function stores information in key-value pair format
  def put(self,key,data):
    index = self.hesh_function(key)
    while self.keys[index] is not None:
      if self.keys[index] == key:
        self.value[index] = data  
        return 
      
      index = (index + 1) % self.size
    self.keys[index] = key
    self.value[index] = data
  
#The function calls the value on the key    
  def get(self,key):
    index = self.hesh_function(key)
    while self.keys is not None:
      if self.keys[index] == key:
        return self.value[index]
      index = (index + 1) % self.size
    return None
    
    
#hesh_function: calculates the ord value of key and   divides by % self.size 
  def hesh_function(self,key):
    sum = 0
    for pos in range(len(key)):
      sum += ord(key[pos])
    return sum % self.size 
  
  
t = Hashtable()
t.put("apple", 10)
t.put("orange", 20)
t.put("banana", 30)
print(t.get("apple"))