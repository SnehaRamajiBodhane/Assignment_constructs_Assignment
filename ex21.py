#21.write a python program to print first 100 and 200 odd numbers?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

print("Using for loop :")
for startrange in range(startrange,endingrange+1):
    if startrange%2!=0:
        print(startrange,end="  ")
print("\n")
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using while loop :")
while startrange<=endingrange:
    if startrange%2!=0:
        print(startrange,end="  ")
    startrange=startrange+1
print("\n")