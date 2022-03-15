#Practical 1
#Write /execute simple ‘Python’ program: Develop minimum 2 programs using Arithmetic Operators, exhibiting data type conversion.

#hello world 
print('Hello, world!')

#arithmatic
num1 = int(2)
num2 = int(3)

print( "addition is : " , num1 + num2)
print( "substract is : " , num1 - num2)
print( "multiply is : " , num1 * num2)
print( "division is : " , num1 / num2)
print( "modules is : " , num1 % num2)
print( "Exponent is : " , num1 ** num2)
print( "Floor Division is : " , num1 // num2)



print("\n")

#The process of converting the value of one data type (integer, string, float, etc.) 
#to another data type is called type conversion. Python has two types of type conversion.

#Implicit Type Conversion : Python automatically converts one data type to another data type. This process doesn't need any user involvement.
#Explicit Type Conversion : users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.

# 1. Implicit Type Conversion
num_int = 12
num_float = 12.01

print("data type of num_int is :", type(num_int))
print("data type of num_float is :", type(num_float))

num_add = num_int + num_float
print("data type of num_sum is :", type(num_add))

print("\n")

# 2. Explicit Type Conversion
num_int = 123
num_string = "123"

print("data type of num_int is :", type(num_int))
print("data type of num_string before type casting is :" , type(num_string))

num_string = int(num_string)
print("data type of num_string after type casting is :" , type(num_string))

num_sum = num_int + num_string

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

print("\n")

