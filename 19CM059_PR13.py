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
list_baby = []
list_school = []
list_adult = []

for i in list1 :
    if(i<=6):
        list_baby.append(i)
    if(i>6 and i<18):
        list_school.append(i)
    if(i>=18):
        list_adult.append(i)

print(list1)
print(list_baby)
print(list_school)
print(list_adult)

print("length of list1 is",len(list1))
print("length of list_baby is",len(list_baby))
print("length of list_school is",len(list_school))
print("length of list_adult is",len(list_adult))
