#7.write a python program to print Natural Number between num1 and num2 where num1>1 num2>2 in reverse order?
num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
print("Using for loop:")

for i in range(num1,num2+1):
    print(num2)
    num2=num2-1

print("Using while loop:")

num1=num2=0
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
while num1<=num2:
    print(num2)
    num2=num2-1