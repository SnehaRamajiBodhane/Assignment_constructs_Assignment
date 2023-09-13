#10.write a python program to print first even number between 100 and 200?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

print("Using for loop :")
for index in range(startrange,endingrange+1):
    if index%2==0:
        print(index,end=" " )
       
print("\n")
j=200
print("Using while loop :")
while startrange<=endingrange:
    if startrange%2==0:
        print(startrange,end="  ")
    startrange=startrange+1
    j=j-1
print("\n")