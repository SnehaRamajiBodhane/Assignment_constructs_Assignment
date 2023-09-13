#11.write a python program to print first even number between 100 and 200 in reverse order?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
x=200
print("Using for loop :")
for i in range(startrange,endingrange+1):
    if x%2==0:
        print(x,end=" " )
    x=x-1
print("\n")
j=200
print("Using while loop :")
while j>=100:
    if j%2==0:
        print(j,end="  ")
    
    j=j-1
print("\n")