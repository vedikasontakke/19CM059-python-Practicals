# practical 7
# Write /execute simple ‘Python’ program: Find the Sum of Digits in a Number

# /  : classic division returns a float
# // : floor division discards the fractional part

num = int(input("enter any random number : "))
sum = 0

while(num > 0):

    mod = num%10
    sum = sum+mod
    num = num//10

print(sum)