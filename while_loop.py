# c = 5
# while c > 0:
#     print(c)
#     c -= 1
#     if c == 3:
        # break
# else:
#     print("in else block")
# print("out")
# sentinal value(-1 or n...)
number = int(input("Enter a number,'-1' to quit:"))
while number != -1:
    print(number)
    number = int(input("Enter a number,'-1' to quit:"))
else:
    print("out of while loop")

