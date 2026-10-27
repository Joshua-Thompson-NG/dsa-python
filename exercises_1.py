# Exercise 1
def non_repeating_char(s: str) -> int:
    my_map = dict()
    for i in s:
        my_map[i] = my_map.get(i,0) + 1

    for i, char in enumerate(s):
        if my_map[char] == 1:
            return i
    return -1

#
# print(non_repeating_char("loveleetcode"))

# Exercise 2
def contains_duplicate(nums: list[int]) -> bool:
    my_map = dict()

    for i in nums:
        if i in my_map:
            return True
        my_map[i] = 1
    return False

    # Another solution
    # if len(nums) == len(set(nums)):
    #     return False
    # return True

print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
