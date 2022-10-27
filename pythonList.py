list = [1, 2, 3, 4, 5]
# Combine arrays
list1 = list + [6, 7, 8]
print(list1)
# list1 += [6, 7, 8]
# Dont list1 + [6, 7, 8]
# Append
list.append(40)
print(list)
# Delete
del list[4]
# list.pop(3)
print(list)

list.remove(40)
print(list)
# Insert
list.insert(4, 10)
print(list)
# Length
print(len(list))
# Combine arrays
list8 = [1, 2, 3]
list9 = [4, 5, 6]
list8.extend(list9)
print(list8)

list9 = [1, 2]
list10 = [3, 4]
list11 = [5, 6]
list12 = list9 + list10 + list11
print(list12)
list13 = [1, 2, 3, 4, 5]
print(3 in list13)
print(500 in list13)

list14 = [1, 20, 3, 4, 20, 5]
print(list14(100))
# Search - Count Method
list15 = [1, 2, 2, 2, 4, 5, 2]
print(list15.count(2))
# Sort Method
list16 = [4, 1, 3, 5, 2]
print(list16.sort())
 
list17 = ["B", "A", "C"]
print(list17.sort())
# Reverse Method
list18 = [1, 2, 3, 4, 5]
print(list18.reverse())