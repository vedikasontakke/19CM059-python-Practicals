#Practical 15
# Functions : Write a program to : To calculate average, mean, median, and standard deviation of numbers in a list
#https://www.mathsisfun.com/data/standard-deviation-formulas.html
#9 2 5 4 12 7 8 11 9 3 7 4 12 5 4 10 9 6 9 4
import math

#average function starts
def avg(list):
    sum=0

    for i in range(0 , len(list)):
        sum = sum+list[i]

    return sum/len(list)

#average function ends

#medium_fun starts

def medium_fun(list):
    medium = len(list)//2
  #  print("medium is ",medium)

    if((len(list)%2) == 0): 
        m =((list[medium]+list[medium+1])/2)
       # print("m is ", m)
        return m
    else:
        return list[medium]

#medium_fun ends

#standard Deviation starts

def standard_deviation_fun(list ,avg):
    add=0
    for i in range(0,len(list)):
       add = add + math.pow((list[i]-avg) , 2)

    standard_deviation = add/len(list)
    return standard_deviation


#standard Deviation starts


#main program starts
list1 = []
length = int(input("enter the length of list :"))
print("enter " , length ," numbers in a list")

for i in range(0,length):
    num=int(input())
    list1.append(num)

avg_list = avg(list1)    
medium_list = medium_fun(list1)
standard_list = standard_deviation_fun(list1 , avg_list)

print("average of list is ",avg_list)
print("mean of list is ",avg_list)
print("medium of list is ",medium_list)
print("standard deviation of list is ",standard_list)





'''
list = []
length = int(input("enter the length of list :"))
print("enter " , length ," numbers in a list")
sum = 0

for i in range(0,length):
    num=int(input())
    list.append(num)
    sum = sum+num

print(list)
avg = sum/len(list)
print("average of elements in a list is ", avg)
print("mean of elements in a list is ", avg)

medium = (len(list)+1)//2
print("medium of elements in a list is ", list[medium-1])

add=0
for i in range(0,length):
    add = add + math.pow((list[i]-avg) , 2)

standard_deviation = add/len(list)
print("standard deviation of list is ", standard_deviation)    
'''
