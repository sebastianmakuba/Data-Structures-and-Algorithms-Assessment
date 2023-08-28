def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != opening_brackets[closing_brackets.index(char)]:
                return False
    
    return not stack

expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1))  
print(is_balanced(expression2))  
