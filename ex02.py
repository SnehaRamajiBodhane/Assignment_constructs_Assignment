# #2 write a python program to print first 20 natural numbers?
# startrange=endingrange=0
# startingrange=int(input("Enter starting range:"))
# endingrange=int(input("Enter ending range:"))
# print("Using for loop :")
# for index in range(startrange,endingrange+1):
#     print(index,end=" " )
# print("\n")


# print("Using while loop:")
# while startrange<=endingrange:
#     print(startrange,end=" " )
#     startrange=startrange+1
# print("\n")

#1.write a python program to print first 20 Natural number except4,7,9?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using for loop :")
for index in range(startrange,endingrange+1):
    if index==4 or index==7 or index==9:
        continue
    print(index,end=" " )
print("\n")

print("Using while loop:")
while startrange<=endingrange:
    if startrange==4 or startrange==7 or startrange==9:
        continue
    print(startrange,end=" " )
    startrange=startrange+1
print("\n")