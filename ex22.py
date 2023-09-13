#22.write a python program to print odd numbers between 100 and 200 reverse order?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

i=200
print("Using for loop :")
for x in range(startrange,endingrange+1):
    if i%2!=0:
        print(i,end="  ")
    i=i-1    
print("\n")
j=200
print("Using while loop :")
while j>=1:
    if j%2!=0:
        print(j,end="  ")
    j=j-1
   
print("\n")
