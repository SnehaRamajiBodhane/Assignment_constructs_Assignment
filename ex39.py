#39.write a python program to print  enven numbers 40 and 80 its squares and cubes in reverse order?
startrange=endingrange=0
startrange=int(input("Enter starting range:"))
endingrange=int(input("Enter ending range:"))

x=80
print("Using for loop :")
for i in range(startrange,endingrange+1):
    if x%2==0:
        print(x,x**2,x**3)
    x=x-1
print("\n")
j=80
print("Using while loop:")
while j>=1:
    if j%2==0:
        print(j,j**2,j**3)
    j=j-1
print("\n")