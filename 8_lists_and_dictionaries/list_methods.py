# Available list methods

"""Adding Elements"""
# append
my_list = [5, 8]
my_list.append(16)
print(my_list)

# extend
my_list.extend([32, 64])
print(my_list)

# insert
my_list = [4, 16]
my_list.insert(1, 8)
print(my_list)

"""Removing Elements"""
# remove the first occurance of argument
my_list = [5, 8, 14, 8]
print("Before remove method: ", my_list)
my_list.remove(8)
print("After remove method: ", my_list)

# pop by default removes element at index -1 and returns that last element; or pop(i) will remove item at position i in list
my_list.pop()
print("After pop method", my_list)
my_list.pop(0)
print("After pop(0) method: ", my_list)
