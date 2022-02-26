# Available list methods

"""Adding Elements"""
# .append(x): Add an item to the end of list.
my_list = [5, 8]
my_list.append(16)
print(my_list)

# .extend(x): Add all items in [x] to list.
my_list.extend([32, 64])
print(my_list)

# .insert(i, x): Insert x into list before position i.
my_list = [4, 16]
my_list.insert(1, 8)
print(my_list)

"""Removing Elements"""
# .remove(x): Remove first item from list with value x.
my_list = [5, 8, 14, 8]
print("Before remove method: ", my_list)
my_list.remove(8)
print("After remove method: ", my_list)

# .pop(): Remove and return last item in list.
my_list.pop()
print("After pop() method", my_list)
# .pop(i): Remove and return item at position i in list.
my_list.pop(0)
print("After pop(0) method: ", my_list)

"""Modifying Elements"""
# .sort(): Sort the items of list in-place.
# Compare to sorted() function (returns sorted list)
my_list = [14, 5, 8]
print("List reset to: ", my_list)
print("Sorted with sorted(): ", sorted(my_list))
my_list = [14, 5, 8]
print("List reset to: ", my_list)
my_list.sort()
print("Result of calling .sort() on prior line: ", my_list)
print("Note: the .sort() method returns None, but the sorted() function returns the sorted list.")

# .reverse(): Reverse the elements of list in-place.
my_list.reverse()
print("Effect of using .reverse() method: ", my_list)

"""Misc"""
# .index(x): Return index of first item in list with value x.
my_list = [14, 5, 8, 5]
print("List reset to: ", my_list)
print("Use .index(value) to return index of value. Returns first occurance if value found more than once. For example, my_list.index(5) returns: ", my_list.index(5))

# .count(x): Count the number of times value x is in list.
my_list = [5, 8, 5, 5, 14]
print("List reset to: ", my_list)
print("Using .count(5) to count number of times 5 is in list: ", my_list.count(5))
