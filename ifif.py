height=int(input("What is your height?"))

if height>=3:
    print("can ride")
    age=int(input("What is your age?"))
    if age<12:
        print("please pay 150 Rs.")
    elif age<=18:
        print("Please pay 250 Rs.")
    else:
        print("Please pay 500Rs.")
else:
    print("Can't ride")
print("bye")