#4.write a python program to print natural number between 100 and 200?
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

#4.1.write a python program to print natural number between 100 and 200 except 10,20,30 order?
startrange=endingrange=0
startingrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using for loop :")

for index in range(startrange,endingrange+1):
    if index==10 or index==20 or index==30:
        continue
    print(index,end=" " )
print("\n")

print("Using while loop:")
while startrange<=endingrange:
    if (startrange==10 or startrange==20 or startrange==30):
        continue
    
    print(startrange,end=" " )
    startrange=startrange+1
    
print("\n")