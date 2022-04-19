#Practical 20
#File Input/output: Write a program to :
#To open a file in read mode and write its contents to another file but replace every occurrence of character ‘h’ by ‘a’.
# To open a file in read mode and print the number of occurrences of a character ‘a’.

# open both files
with open('19CM059_PR20.txt','r') as firstfile, open('19CM059_PR20_B.txt','a') as secondfile:
