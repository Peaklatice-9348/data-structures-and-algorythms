from stack import Stack
stack = Stack(20)
opening_brakets = ['(','{','[']
closing_brakets = [')','}',']']
expression = input('Enter expression here:')
for i in range(len(expression)):
    if expression[i] == '(' or expression[i] == '[' or expression[i] == '{':
        stack.push(expression[i])
    elif expression[i] == ')' or expression[i] == ']' or expression[i] == '}':
        if closing_brakets.index(expression[i]) == opening_brakets.index(stack.get(-1)):
            stack.pop()
if len(stack.list) == 0:
    print('works')
else:
    print('doesnt works')

