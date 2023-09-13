#13.write a python to print sum of first 20 even number ?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
sum=0
print("Using for loop :")
for startrange in range(startrange,endingrange+1):
    if startrange%2==0:
        sum=sum+startrange
    startrange=startrange+1   
print("Sum:",sum)
print(startrange,end=" " )
 
       
print("\n")
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

sum=0
print("Using while loop :")
while startrange<=endingrange:
    if startrange%2==0:
        sum=sum+startrange
    startrange=startrange+1
print("Sum:",sum)
print(startrange,end="  ")

print("\n")