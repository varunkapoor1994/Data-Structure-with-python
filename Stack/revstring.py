from stack import Stack
def revString(input: str) -> str:
    a=Stack()
    rev=""
    for i in input:
        a.push(i)
    print(a.viewAll())
    while not a.isEmpty():
        rev+=a.pop()
    return rev

print(revString("abc"))