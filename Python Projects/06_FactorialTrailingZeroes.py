# Calculate the number of trailing zeroes in that factorial.
# Trailing Zeroes - The number of zeroes at the end of a number
def factorialTrailingZeroes(number):
    count = 0
    i = 5
    while (number//i != 0):
        count += (number/i)
        i = i*5
    return count
b=int(input('Enter a number : '))
print(factorialTrailingZeroes(b))