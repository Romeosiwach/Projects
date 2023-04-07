# Factorial using Recursion Function
def fact(a):
    if a == 0:
        return 1
    elif a < 0:
        return "Invalid"
    else:
        return a*fact(a-1)


a = int(input('Enter the number : '))
print(fact(a))
