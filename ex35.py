#35.write a python program to print first 20  odd numbers its squares and cubes in reverse order?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

x=20
print("Using for loop :")
for i in range(startrange,endingrange+1):
    if x%2!=0:
        print(x,x**2,x**3)
    x=x-1
print("\n")
j=20
print("Using while loop:")
while j>=1:
    if j%2!=0:
        print(j,j**2,j**3)
    j=j-1
