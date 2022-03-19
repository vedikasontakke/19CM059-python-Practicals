# practical 8
# Write /execute simple ‘Python’ program: Print all Numbers in a Range Divisible by a Given Number

num = int((input("enter a number : ")))

for i in range(1,100) :
    if(i % num == 0) :
        print(i)
    