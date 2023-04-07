# Make a program for receipt maker in a grocery shop
sum = 0
while (True):
    a = (input('User_input :'))
    if a != "q":
        sum = sum + int(a)
        print(sum)
    else:
        print('Thanks for shopping with us!')
        break
