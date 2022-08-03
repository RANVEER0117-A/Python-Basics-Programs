# Pythin program to find out the area of a triangle
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# Semi perimeter
s = (a + b + c) / 2  
  
# Area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)  