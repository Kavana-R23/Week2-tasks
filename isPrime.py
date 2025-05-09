def isPrime(num):
    if num<=1:
        return False
    for i in range (2,num):
        if num % i==0:
            return False
        
    return True

isPrime(5)
isPrime(10)