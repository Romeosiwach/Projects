# Making a calculaotr which takes input from user and provides result until q key is pressed

while (True):
    a = int(input('Enter the first number : '))
    b = int(input('Enter the second number : '))
    calculation = input("Choose the mode of calculation (+,-,*,/,%) : ")
    for i in calculation:
        if i == ('+'):
            print('Sum of the numbers is : ', (a+b))
        elif i == ('-'):
            print('Substraction of the  numbers is : ', (a-b))
        elif i == ('*'):
            print('Multiplication of the numbers is : ', (a*b))
        elif i == ('/'):
            print('Division of the numbers is : ', (a/b))
        elif i == ('%'):
            print('Mode of the numbers is : ', (a % b))
        elif i == ('q'):
            print('Exit')
        else:
            print("Thanks for using our calculator")
