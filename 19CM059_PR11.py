# practical 11
# Write /execute simple ‘Python’ program: Remove the Duplicate Items from a List

my_list = [ 2 , 6  , 10 , 2 , 1 , 7 , 1 , 4]
print(my_list)

my_list = list(dict.fromkeys(my_list))
print(my_list)