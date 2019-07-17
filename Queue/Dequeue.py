from dataclasses import dataclass,field
from typing import Any,List
def default_val():
    return []

@dataclass
class Dequeue:
    items:List[Any]=field(default_factory=default_val)
    def isEmpty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.insert(0,item)
    def addRear(self,item):
        self.items.append(item)
    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()
    def viewAll(self):
        return self.items
    def size(self):
        return len(self.items)

#deq=Dequeue()
#deq.addFront(5)
#deq.addFront(4)
#deq.addFront(3)
#print(deq.viewAll())
#print(deq.removeFront())
#print(deq.viewAll())
#print(deq.removeRear())
#print(deq.viewAll())
#deq.addRear(6)
#print(deq.viewAll())



    
