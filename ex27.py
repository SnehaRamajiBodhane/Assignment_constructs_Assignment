#27.write a python program to print Product of first 20 odd numbers?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
product=1
print("Using for loop :")
for startrange in range(startrange,endingrange+1):
    if startrange%2!=0:
        product=product*startrange
    startrange=startrange+1   
print("Product:",product)
print(startrange,end=" " )
 
       
print("\n")

startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
product=1
print("Using while loop :")
while startrange<=endingrange:
    if startrange%2!=0:
        product=product*startrange
    startrange=startrange+1
    
print("Product:",product)
print(startrange,end="  ")
