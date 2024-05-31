height=int(input("What is your height?"))
bill=0
if height>=3:
    print("can ride")
    age=int(input("What is your age?"))
    if age<12:
        bill=150
        print("ticket price is 150 Rs.")
    elif age<=18:
        bill=250
        print("ticket price is 250 Rs.")
    else:
        bill-500
        print("ticket price is 500Rs.")
    want_photo=input("Do you want to take a photo(Y/N)?")
    if want_photo=='Y' or want_photo=='N':
        bill=bill+50
    print(f"Your total bill is {bill}")
else:
    print("Can't ride")
print("bye")