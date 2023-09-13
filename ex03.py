#3.write a python to print first 20 Natural Numbers in reverse order except 3,6,8,9?
startingrange=endingrange=0
startingrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using for loop :")
i=20
for index in range(startingrange,endingrange+1):
    print(i,end=" ")
    i=i-1
print("\n")

j=20
print("Using while loop:")
while startingrange<=20:
    print(j,end=" " )
    startingrange=startingrange+1
    j=j-1
print("\n")






#3.write a python to print first 20 Natural Numbers in reverse order?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using for loop :")
i=20
for index in range(startrange,endingrange+1):
    print(index,end=" ")
    iindex=index-1
print("\n")

j=20
print("Using while loop:")
while j>=1:
    print(j,end=" " )
    
    j=j-1
print("\n")

