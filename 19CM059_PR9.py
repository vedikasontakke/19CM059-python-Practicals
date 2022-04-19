# practical 9
# Using List: Write a programs to: Create a list, add element to list, delete element from the list. Sort the list, reverse the list
# and counting elements in a list

# create list 
my_list = ["cloud computing" , "python" , "linux" , "java" , "data structure"]

# add element at last index
my_list.append("operating system")
print(my_list)

#add element at given index 
#my_list.insert(1, "php")
my_list[3] = "llb"
print(my_list)

#remove element from list
my_list.remove("llb")       
print(my_list)
my_list.pop(1)
# sort the list
my_list.sort()
print(my_list)

#reverse the list 
my_list.reverse()
print(my_list)

# counting elements 
print(len(my_list))
print(max(my_list))