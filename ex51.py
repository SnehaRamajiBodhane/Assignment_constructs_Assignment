# 51.write a program to display alphabets as given below?
#AZ BY CX DW EV FU GT HS IR KP LO MN OL  PK QJ RI SH TG UF VE WD XC YB ZA

n = 26  # Number of alphabets
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
for i in range(n):
    line = ""
    for j in range(n):
        if j % 2 == 0:
            line += alphabets[(i + j) % n]
        else:
            line += alphabets[(n - i - 1 + j) % n]
            print(line)


n = 26  # Number of alphabets
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0

while i < n:
    line = ""
    j = 0
    while j < n:
        if j % 2 == 0:
            line += alphabets[(i + j) % n]
        else:
            line += alphabets[(n - i - 1 + j) % n]
        j += 1
        print(line)
        i += 1