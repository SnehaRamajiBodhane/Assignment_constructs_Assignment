#28.write a python program to print sum of odd number between 10 and 20?
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

   
    
print("\n")

#28.1.write a python program to print sum of odd number between 10 and 20?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))
product=1
print("Using for loop :")
for startrange in range(startrange,endingrange+1):
    if startrange%2!=0:
        if (startrange==13 or startrange==17 or startrange==19):
            continue
        product=product*startrange
    startrange=startrange+1 
    startrange=startrange-1  
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
        if (startrange==13 or startrange==17 or startrange==19):
            continue
        product=product*startrange
    startrange=startrange+1 
      
       
print("Product:",product)
print(startrange,end="  ")

   
    
print("\n")