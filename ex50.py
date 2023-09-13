#50.write a program to display alphatbets as given below?
# Z, Y, X, W, V, U, T, S, R, Q, P, O, N, M, L, K, J, I, H, G, F, E, D, C, B, A
x=90
print("Using for loop:")
for i in range(65,91):
    print(chr(x), end=" ") 
    x=x-1
print("\n")






j=90
print("Using while loop:")
while j>=1:
    print(chr(j), end=" ") 
    j=j-1
    
print("\n")
