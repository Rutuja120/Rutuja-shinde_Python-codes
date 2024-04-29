x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

# Python Program to find the area of triangle

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# Python program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print(" factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

 # python code for sum of n natural numbers.
num = int(input("Enter a number : "))
sum = 0
for i in range(num+1):
  sum+=i
print(sum)  

print( "after swapping value of x : ", x  and y , y ) 
print('The area of the triangle is %0.2f' %area)  
print("The factorial of",num,"is",factorial)         
print("sum_first_n_numbers", sum)  





