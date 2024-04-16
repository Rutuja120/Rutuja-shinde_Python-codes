message = input("Enter message : ")
i = 1
while (i <= 10):
    print(message, i, " times")
    i=i+1

num = int(input("Enter value for  num : "))
i = 1
result = 0
while(i <= 10):
    result = num * i
    print (num, "*" "=", i, "=", result)
    i = i+1
    
#print reverse of a number
num = int(input("Enter the integer number: "))  
  
revs_num = 0  
  
while (num > 0):  
    remainder = num % 10  
    revs_num = (revs_num * 10) + remainder  
    num = num // 10  
  
print("The reverse number is :",revs_num) 
