# Exercise 1
def valid_parentheses(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []
    hashMap = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in hashMap:
            if stack:
                top_element = stack.pop()
            else:
                top_element = "#"
            if hashMap[i] != top_element:
                return False
        else:
            stack.append(i)
    return len(stack) == 0

# print(valid_parentheses("()[]{}")) # True
# print(valid_parentheses("(]")) # False
# print(valid_parentheses("([)]")) # False


