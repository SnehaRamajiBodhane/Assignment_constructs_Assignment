# #9.write a python program to prim first 20 even numbers?
# startrange=endingrange=0
# startrange=int(input("Enter starting range:"))
# endingrange=int(input("Enter ending range:"))

# print("Using for loop :")
# for index in range(startrange,endingrange+1):
#     if index%2==0:
#         print(index,end=" " )
        
# print("\n")
# j=20
# print("Using while loop :")
# while startrange<=endingrange:
#     if startrange%2==0:
#         print(startrange,end="  ")
#     startrange=startrange+1
   
# print("\n")
#9.1.write a python program to prim first 20 even numbers in reverse order except?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
i=20
print("Using for loop :")
for i in range(startrange,endingrange+1):
    if i%2==0:
        print(i,end="  ")
        i=i-1
print("\n")
j=20
print("Using while loop :")
while j>=1:
    if j%2==0:
        print(j,end="  ")
    j=j-1
   
print("\n")
