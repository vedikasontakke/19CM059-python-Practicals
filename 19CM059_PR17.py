#Practical 17
# Exception Handling: Write a program to : To handle simple runtime error To handle multiple errors with one except statement
import math

num = 4
list = [1 , 2]
hello = "hell0"
'''
try:
    print(num/1)
    print(list[0])
    print(math.sqrt(-2))
    print(hello/1)
except ZeroDivisionError:
    print("zero divisor error  occour")  
except IndexError:
    print("array index out of bound")
except TypeError:
    print("type error occoured")    
except ValueError:
    print("value error occoured")    
'''


try:
    print(num/0)
    print(list[2])
    print(math.sqrt(-2))
    print(hello/1)
except (ZeroDivisionError , IndexError ,TypeError , ValueError):
    print("error")  


