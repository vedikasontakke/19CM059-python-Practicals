#Practical 5
#Write /execute simple ‘Python’ program: calculate the area and perimeter of the Square, and the volume & perimeter of the cone
import math

side = 20
print("Area of square is: ", side*side)
print("Perimeter of square is: ", side*4)

radius = 2
height = 5 

print("Perimeter of cone is: ",2*(math.pi)*radius)
print("Volume of cone is: " , (math.pi)*(radius*radius)*(height/3))