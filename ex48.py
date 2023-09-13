#48.write a program that asks the user for a positive integer value.The program should calculate the sum of all the integers from 1 up the number entered except 4,6,9,11,13.
#for example,if the user enters 20,the loop will find the sum of 1,2,3,4...20?ex47.py
num=int(input("Enter positive integer number:"))
result=0
for i in range(21):
      if (i==1 or i==2 or i==3 or i==4):
           continue
   digit=num%
    num=num//i
 print("sum is:",result)
while num>0:
    digit=num%20
    result = result + digit 
    num = num//20
print("sum is:",result)
