from typing import List

def reverseItNow(stack,top):
    if len(stack) == 0:
        stack.append(top)
        return
    
    t = stack[-1]
    stack.pop()
    reverseItNow(stack,top)
    stack.append(t)

def reverseStack(stack: List[int]) -> None:
    # Write your code here.
    if len(stack) == 0:
        return
    top = stack[-1]
    stack.pop()
    reverseStack(stack)
    reverseItNow(stack,top)
    return stack

print(reverseStack([1,2,3,4,5,6]))