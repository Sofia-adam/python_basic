n = int(input("enter a number:"))

for i in range(1,n+1):
    cn = i
    fact = 1
    for j in range(1,cn+1):
        fact = fact*j
    print(cn,":",fact)