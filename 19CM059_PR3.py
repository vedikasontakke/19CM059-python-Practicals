#Practical 3
#Write /execute simple ‘Python’ program: Calculate the Average of Numbers in a Given List

list_no = [22 , 35 , 40 , 2 , 0]
sum = 0

for i in list_no :
    sum = sum + i 

avg = sum/len(list_no)
print(avg)