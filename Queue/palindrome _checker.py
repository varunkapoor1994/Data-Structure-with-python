from Dequeue import Dequeue
def check_palindrome(input_string:str)-> bool:
    for i in input_string:
        queue.addRear(i)
    while queue.size() > 1:
        if queue.removeFront().lower()==queue.removeRear().lower():
            continue
        break
    if queue.size()>1:
        return False
    return True

#print(check_palindrome("Naman"))
#queue=Dequeue([char for char in "input"])
#print(queue.viewAll())