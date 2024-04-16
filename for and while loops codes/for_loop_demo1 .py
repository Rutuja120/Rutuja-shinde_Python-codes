#demo for loop + range function

"""for i in range(0, 10+1, 1):
    print(i)"""


"""start = int(input("Enter value for start : "))
stop = int(input("Enter value for stop : "))
step = int(input("Enter value for step : "))

for i in range(start, stop, step):
    print("Hello All.....!",i)"""


#print summation of first - n numbers :
"""n =int(input("Enter value for n : ")) 
sum = 0
for i in range(1, n+1, 1):
    sum += i
print("Summation : ", sum)"""


#print table of a given number, take the number  from user.
# num = 5 --> 5* 1 = 5

"""num = int(input("Enter a number to print  multiplication table: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

print("Multiplication table for", num, ":")"""

#print the even numberslist till 50.


"""for i in range(1, 51, 1):
    if(i%2 == 0):
        print("Even numbers",i)"""

#print the factorial of a given number

num = int(input("Enter value for num : "))
fact = 1
for i in range(1, num+1, 1):
    fact *= i
print("Factorial of  num is : ",  fact)









