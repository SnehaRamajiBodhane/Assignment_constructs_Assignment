# #8.write a python program to prim first 20 even numbers?
# startrange=endingrange=0
# startrange=int(input("Enter starting range:"))
# endingrange=int(input("Enter ending range:"))

# print("Using for loop :")
# for index in range(startrange,endingrange+1):
#     if index%2==0:
#         print(index,end=" " )
    
# print("\n")


# print("Using while loop:")
# while startrange<=20:
#     if startrange%2==0:
#         print(startrange,end=" " )
#     startrange=startrange+1
# print("\n")

#8.1.write a python program to prim first 20 even numbers except4,8,12?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

print("Using for loop :")
for index in range(startrange,endingrange+1):
    if index%2==0:
        if(index==4 or index==8 or index==12):
            continue
        print(index,end=" " )

print("\n")
j=20
print("Using while loop:")
while startrange<=endingrange:
    if startrange%2==0:
        if(j==4 or j==8 or j==12):
            continue
        print(startrange,end=" ")
    startrange=startrange+1
    j=j-1
print("\n")
