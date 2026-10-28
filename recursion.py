# RECURSION

# A function that calls itself to solve smaller problems.

# Two rules of recursion

# 1. Base Case (Smallest doll) - The stopping condition for the recursion
# 2. Recursive Case (Opening the next doll) - The function calls itself to solve smaller problems

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)