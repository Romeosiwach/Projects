    # BEST TYPE FABONACCI SERIES PRINTING  
num=int(input('Enter the number : '))
n1,n2=0,1
print('Fibonacci series : ',n1,n2, end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    
    print(n3)
print()

   # FABONACCI SERIES PRINTING USING YIELD KEYWORD
# def fibonacci():
#     a,b=0,1
#     while(True):
#         yield a
#         a,b=b,a+b

# f1= fibonacci()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))