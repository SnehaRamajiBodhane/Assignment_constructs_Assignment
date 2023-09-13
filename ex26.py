#26.write a python program to print odd number between num1 and num2 where num1>1 num2>2 in reverse order?
num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
print("Using for loop:")
sum=0

for num2 in range(num1,num2+1):
    if num2%2==0:
        sum=sum+num2
    num2=num2+1
    num2=num2-1
print("Sum:",sum)
print(num2)

print("Using while loop:")
num1=num2=0
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

sum=0
print("Using while loop :")
while num1<=num2:
    if num1%2==0:
        sum=sum+num1
    num1=num1+1
   
print("Sum:",sum)
print(num1,end="  ")
num1=num1-1
   
