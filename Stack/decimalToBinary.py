from stack import Stack
def binaryToDecimal(num : int) -> str:
    binary=""
    binary_stack=Stack()
    while num > 0:
        binary_stack.push(num%2)
        num=int(num/2)
    while not binary_stack.isEmpty():
        binary+=str(binary_stack.pop())
    return binary

a=input("Enter the decimal number : ")
print(binaryToDecimal(int(a)))
