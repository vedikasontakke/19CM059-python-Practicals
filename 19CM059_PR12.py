# practical 12
# Using Dictionary: Write a programs to:
#(i) Create dictionary, add element to dictionary, delete element from the dictionary

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


#create dictionary 
my_dist = {

    "name" : "jethalal" ,
    "surname" : "gada"  ,
    "age" : 42 ,
    "favorite_dish" : "jelebi fafda"
}

print(my_dist)

# add items 
my_dist["favorite_person"] = "babitaji"
print(my_dist)

#remove items
my_dist.pop("age")
print(my_dist)

del my_dist  #completly delete dict 
