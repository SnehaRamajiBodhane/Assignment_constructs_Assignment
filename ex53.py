# 53.write a program to display alphabets as given below?
#z y x w v u t s r q p o n m l k j i h g f e d c b a 
i=122
print("Using for loop:")
for x in range(97,123):
    print(chr(i), end=" ") 
    i=i-1
print("\n")




j=122
print("Using while loop:")
while j>=1:
    print(chr(j), end=" ") 
    j=j-1
    
print("\n")
