#write a python program to print the message "I Can do it today itselft." 10 times?
startrange=endingrange=0
startingrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
print("Using for loop :")
for index in range(startrange,endingrange+1):
    print("I Can do it today itselft." )


print("Using while loop:")
while startrange<=endingrange:
    print("I Can do it today itselft." )
    startrange=startrange+1

