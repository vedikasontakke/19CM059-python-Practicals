#Practical 18
# File Input/output: Write a program to : Python Program to Read the Contents of a File

a = str(input("enter the name of file wih .txt extensions : "))
file2 = open(a , 'r')
line = file2.readline()

while(line != ""):
    print(line)
    line = file2.readline()
file2.close()    
