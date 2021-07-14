# a = [i for i in range(100) if i > 10 if i < 50]
# print(a)

# non_flat = [ [1,2,3], [4,5,6], [7,8] ]
# list1 = [ y for x in non_flat if len(x) > 2 for y in x ]
# print(list1) # [1, 2, 3, 4, 5, 6]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)