count = 0
char = input("ENTER CHARACTER TO COUNT IN FILE:")
file = open("19CM059_PR20.txt", "r")
for i in file:
    for c in i:
        if c == char:
            count = count + 1
print("THE CHARACTER {} IS FOUND {} TIMES IN THE TEXT FILE".format(char, count))