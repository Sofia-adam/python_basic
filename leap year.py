year = int(input("enter a year:"))

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("the given year is a leap year")
else:
    print("the given year is a leap year")