# practical 11
# Write /execute simple ‘Python’ program: Remove the Duplicate Items from a List

my_list = [ 2 , 6  , 10 , 2 , 1 , 7 , 1 , 4]
print(my_list)

my_list = list(dict.fromkeys(my_list))
print(my_list)


a = [10,20,30,20,10,50,60,40,80,50,40]

uniq_items = []
for x in a:
    if x not in uniq_items:
        uniq_items.append(x)

print(uniq_items)



duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))