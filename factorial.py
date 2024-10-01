# calculate the factorial of the input
# find the no of the trailing zero in a factorial

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)
def factorialoftrailingzeros(number):
    fac = factorial(number)
    while(number%10==0):
        count = 0
        fac = fac/10
    return count


if __name__ == '__main__':
    number=int(input("enter any number"))
    fac= factorial(number)
    print(f"The factorial of a number is {fac}")
    print(f"the no of trailing zeros in a factorial is {fac}")