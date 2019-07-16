from dataclasses import dataclass,field
from typing import List,Any
def default_val():
    return []
@dataclass
class Queue:
    items:List[Any]=field(default_factory=default_val)
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def viewAll(self):
        return self.items

queue=Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print(queue.viewAll())
print(queue.dequeue())

    