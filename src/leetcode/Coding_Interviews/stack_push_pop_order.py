# -*- coding: utf-8 -*-


def validate_stack_sequences(pushed: [int], popped: [int]) -> bool:
    stack, i = [], 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1

    return not stack
