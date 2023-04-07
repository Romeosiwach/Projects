# FIBONACCI SERIES USING RECURSION FUNCTION
def fibo(n):
    if n <= 1:
        return n
    elif n<0:
        return ('Invalid! enter positive intiger')
    else:
        return (fibo(n-1)+fibo(n-2))
    
a=int(input('Enter the number'))
print(f'Fibonacci series of first {a} numbers is : ')
for i in range(a):
    print(fibo(i))


# FACTORIAL USING RECURSION
# def fact(n):
#     if n < 0:
#         return 'invalid'
#     elif n == 0:
#         return 1
#     else:
#         return n*fact(n-1)


# a = int(input('Enter the number : '))
# print(f'The factorial of {a} is : ', fact(a))
