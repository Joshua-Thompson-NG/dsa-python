# Exercise 1
def power_of_two(n: int) -> bool:
    if n <= 0:
        return False # Negative Numbers
    if n == 1:
        return True # 2^0 = 1

    if n % 2 != 0:
        return False # Odd Numbers that isn't one can't be a power of 2

    return power_of_two(n//2)

print(power_of_two(3))

# Exercise 2
def f(n: int) -> int:
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    return f(n-1) + f(n-2)

print(f(4))