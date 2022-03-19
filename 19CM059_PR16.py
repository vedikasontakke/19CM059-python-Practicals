#Practical 16
# Functions : Write a program to : To print Factors of a given Number.

def factors(n):
    for i in range(1 , n+1):
      if(n%i == 0):
        print(i)
 

num=int(input("enter a number : "))
print("factors of ",num," are :")
factors(num)
