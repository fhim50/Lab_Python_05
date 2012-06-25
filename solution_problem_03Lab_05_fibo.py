#for k in range(1,n+1):
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
        
