#Practical 19
# File Input/output: Write a program to : To create simple file and write “Hello World” in it. To opens a file in write mode and 
# append Hello world at the end of a file.

# to create a new file and write in it 
with open('19CM059_PR19.txt', 'w') as f:
    f.write('Hello World')