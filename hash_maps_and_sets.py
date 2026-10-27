# HASH MAPS AND SETS

# Hash maps and sets are arguably the most important data structures for coding
# interviews.
# While arrays and linked lists require you to search through them sequentially
# (taking $O(N)$ time), hash-based structures allow you to look up, insert, and
# delete data almost instantly in $O(1)$ time.


# Hash maps are used to store key-value pairs.
# When you add a key-value pair, the hash map takes the key and runs it through a
# mathematical formula called a hash function. This function converts the key
# into an integer index, which tells the computer exactly which "bucket"
# (memory location) to store the value in. Because the math tells the computer
# exactly where to look, it doesn't need to scan through the whole structure to
# find your data.
# Initialization
my_map = {} # or dict()

# Insertion / Updating
my_map["apple"] = 5
my_map["banana"] = 2
my_map["apple"] = 10 # Overwrites the previous value

# Retrieval
print(my_map["apple"]) # Output: 10

# Check if a key exists (Extremely common in LeetCode)
if "banana" in my_map:
    print("Banana is here!")

# Deletion
del my_map["apple"]

# Iteration
for key, value in my_map.items():
    print(f"{key} -> {value}")

# Hash sets are used to store unique values.
# A set is basically a hash map that only stores keys, no values.
# It is an unordered collection of unique elements.

# Initialization
my_set = set() # Note: {} creates an empty dictionary, not a set!

# Insertion
my_set.add(1)
my_set.add(2)
my_set.add(1) # Ignored, 1 is already in the set

# Retrieval / Checking existence
if 2 in my_set:
    print("2 is in the set") # Output: 2 is in the set

# Deletion
my_set.remove(2)

# Iteration
for item in my_set:
    print(item)

