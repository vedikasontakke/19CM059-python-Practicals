# practical 10
# Write /execute simple ‘Python’ program: Merge Two Lists and Sort it

list_1 = [2 , 4 , 6 , 8 , 10 ]
list_2 = [1 , 3 , 5 , 7 , 9]

print(list_1)
print(list_2)

# 1 method to merge list
merge_list = list_1 + list_2
print(merge_list)

# 2 method to merge list
list_1.extend(list_2)
print(list_1)

# sort list
merge_list.sort()
print(merge_list)


# 3 method to merge list
for x in list_2:
  list_1.append(x)

print(list_1)