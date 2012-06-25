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
