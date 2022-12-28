"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1)
Input: s = "()[]{}"
Output: true

Example 2)
Input: s = "(]"
Output: false
"""

def isValid(s: str) -> bool:
    """
    bracket의 k-v 쌍과 Stack 구조를 활용

    Stack 구조를 사용한 이유는?
    :Open bracket의 역순으로 닫아줘야 하기 때문에 Stack 구조를 활용(LIFO)

    elif 문은 Close bracket이 없거나 그 key-value 쌍이 맞지 않는 경우를 뜻함
    """
    bracket_set = {
        "(":")",
        "{":"}",
        "[":"]",
    }

    stack = []
    for char in s:
        if char in bracket_set:
            stack.append(char)
        elif not stack or bracket_set[stack.pop()] != char:
            return False
    
    return not stack
