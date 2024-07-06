m = int(input("enter your marks:"))

if m < 35:
    print("Grade 'F' : Fail")
elif m>=35 and m<=40:
    print("Grade D")
elif m>=41 and m<50:
    print("Grade C")
elif m>=41 and m<60:
    print("Grade B")
elif m>=41 and m<70:
    print("Grade B+")
elif m>=41 and m<80:
    print("Grade A")
else:
    print("Grade A+")

