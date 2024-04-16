#palindrome number

n=int(input("Enter number:"))
temp=n
rem = 0
reverse=0
while(n>0):
    rem = n%10
    reverse = reverse * 10+rem
    n=n//10
if(temp==reverse):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")