#Practical 21
# Write a program to Count the Number of Words in a Text File

fname = input("enter the name of file :")

num_words = 0
with open(fname , 'r') as f :
    for line in f :
        words = line.split()
        num_words += len(words)
print("number of words")
print(num_words)        