fact = 1       #initialising a variable fact equal to 1
n = int(input("enter a number:")) #taking output from the user

for i in range(1,n+1): #using for loop for the iterating for no of times
    fact = fact*i      #storing the output in the fact variable
print("factorial of given number",n,"is",fact) #printing the output