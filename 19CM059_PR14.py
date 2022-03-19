# practical 14
# Looping: Write a program to : Find factorial of a given number.
# Generate multiplication table up to 10 for numbers 1 to 5

num = int(input("enter a number:"))
factorial = 1

if(num < 0):
    print("factorial ")
for i in range(1 , num+1):
    factorial = factorial * i

print("factorial of ", num , " is ",factorial)    

print("tables from 1 to 5 are :")

for i in range(1 , 5+1):
    for j in range(1 , 10+1):
        print(i," * ",j," = ",i*j)
    print(" ")    