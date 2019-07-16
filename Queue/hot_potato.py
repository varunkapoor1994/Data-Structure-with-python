from Queue import Queue
from typing import List
def hot_potato(nameList:List,num:int)->str:
	nameQueue=Queue(nameList)
	print(nameQueue.viewAll())
	while nameQueue.size() >1:
		for i in range(0,num):
			nameQueue.enqueue(nameQueue.dequeue())
		nameQueue.dequeue()
	return nameQueue.viewAll()
			


names=["Varun","Manik","Sagar","Aparna","deepen","Sonali"]
final=hot_potato(names,3)
print(final)