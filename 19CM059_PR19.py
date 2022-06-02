#Practical 19
# File Input/output: Write a program to : To create simple file and write “Hello World” in it. To opens a file in write mode and 
# append Hello world at the end of a file.

# to create a new file and write in it 
#with open('ved.txt', 'a') as f:
 #   f.write('Hello World')


f = open("dummy.txt", "w")
f.write("Hello World")
f.close()

# open a file in write mode
f = open("dummy.txt", "w")
print(f.write("hello world"))

# open a file in append mode
f = open("dummy.txt", "a")
f.write("\nHello World")
f.close()

# read content of file
f = open("dummy.txt", "r")
print(f.read())   