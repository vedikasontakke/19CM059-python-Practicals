# Practical 13
# Looping: Write a program to : To print all prime numbers from 1 to N.
#To read age of 15 person and count total Baby age, School age and Adult age.

start = int(input("enter starting point :"))
end = int(input("enter end point :"))

for i in range(start , end ) :
    llb = 2
    flag = 0
    while(llb < i):
        if(i % llb == 0):
            flag = 1
            break
        
        llb += 1
    if(flag == 0):
        print(i)   


list1 = [1 , 2 , 4 , 6 , 12 , 18 , 21 , 15 , 8 , 3 , 5 , 17 , 16 , 15 , 10]
