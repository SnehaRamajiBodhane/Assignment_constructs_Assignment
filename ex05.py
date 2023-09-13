# #5.write a python program to print natural number between 100 and 200 in reverse order ?
# startrange=endingrange=0
# startingrange=int(input("Enter starting range:"))
# endingrange=int(input("Enter ending range:"))
# i=200
# print("Using for loop :")
# for index in range(startrange,endingrange+1):
#     print(i,end=" " )
#     i=i-1
# print("\n")

# j=200
# print("Using while loop:")
# while startrange<=endingrange:
#     print(startrange,end=" " )
#     j=j-1
#     startrange=startrange+1
# print("\n")

#5.1.write a python program to print natural number between 100 and 200 in reverse order except 11,21,31,41,51,61,71,81,91,101,111,121,131,141 ?
startrange=endingrange=0
startingrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
i=200
print("Using for loop :")
for i in range(startrange,endingrange+1):
    if (i==11 or i==21 or i==31 or i==41 or i==51 or i==61 or i==71 or i==81 or 
        i==91 or i==101 or i==111 or i==121 or i==131 or i==141):
        continue
    print(i,end=" " )
    i=i-1
print("\n")

j=200
print("Using while loop:")
while startrange<=endingrange:
    if (startrange==11 or startrange==21 or startrange==31 or startrange==41 or startrange==51 or startrange==61 or startrange==71 or startrange==81 or 
        startrange==91 or startrange==101 or startrange==111 or startrange==121 or startrange==131 or startrange==141):
        continue
    print(j,end=" " )
    startrange=startrange+1
    j=j-1
print("\n")