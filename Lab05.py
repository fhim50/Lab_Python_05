


#problem2
def factorial(number):
    #
    factorial = 1
    if number<0:
        print 'invalid number'
    else:
        for k in range(1,number+1):
            factorial=factorial*k
        return factorial

# problem3
def fib(n):
    
    if n == 0:
            return 0
    elif n == 1:
         return 1
    else:
        return fib(n-1)+fib(n-2)
def fibonacci(n):
    list =[]
    for k in range(1,n+1):
        list.append(fib(k))
    return list
        

#problem4
def prime(number):
    number*=1
    prime = True
    for divisor in range(2,number):
        if number/divisor == int(number/divisor):
            prime=False
    if prime == False:
        print number , '  is not prime'
    else:
        print number,'  is prime '

      
