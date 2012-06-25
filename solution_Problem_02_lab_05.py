
def factorial(number):
    #
    factorial = 1
    if number<0:
        print 'invalid number'
    else:
        for k in range(1,number+1):
            factorial=factorial*k
        return factorial
'''
def fact(number):
    fact = 1
    if number<0:
        print 'invalid number'
    else:
        while number :
            fact = fact * number
            number=number-1
        return fact
'''
