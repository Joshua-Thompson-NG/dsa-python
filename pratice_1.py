my_map = dict()

my_map["apple"] = 2
my_map["banana"] = 3
my_map["apple"] = 4
my_map["orange"] = 5

print(my_map["apple"])

if "banana" in my_map:
    print("yes")

del my_map["apple"]

print(my_map)

for k,v in my_map.items():
    print(k,v)

