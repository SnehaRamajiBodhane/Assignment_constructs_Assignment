#write a python program to print product of even number between num1 and num2 where num1>1 num2>2 in reverse order?
num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
print("Using for loop:")
product=1
for i in range(num1,num2+1):
    product=product*i
    print(num2)
    print(product)
    num2=num2-1

print("Using while loop:")
product=1
num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
while num1<=num2:
    product=product*num1
    num1=num1+1
    print(num2)
    print(product)
    num2=num2-1