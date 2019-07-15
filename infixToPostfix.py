from stack import Stack
def infix_to_postfix(inputExpression:str) ->str:
    operatorStack=Stack()
    postfixExpression=""
    for token in inputExpression:
        if ord(token) in range(65,90) or ord(token) in range(48,57):
            postfixExpression+=token
        elif token == ")":
            while True:
                if operatorStack.peek()=="(":
                    operatorStack.pop()
                    break
                else:
                    postfixExpression+=operatorStack.pop()

        else:
            operatorStack.push(token)
    while not operatorStack.isEmpty():
        postfixExpression+=operatorStack.pop()
    return postfixExpression
        
            


print(infix_to_postfix("((A+B)—C*(D/E))+F"))