from dataclasses import dataclass
from typing import Any

@dataclass
class ListNode:
    data:Any=None
    next:Any=None
    def has_value(self,value):
        return self.data==value


@dataclass
class SinglyLinkedList:
    head:Any=None
    tail:Any=None
    def add_list_item(self,item):
        if not isinstance(item,ListNode):
            item=ListNode(item)
        if self.head is None:
            self.head=node
        else:
            self.tail.next=node
        self.tail=node
        return
        