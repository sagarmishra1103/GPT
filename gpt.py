#print("hi, this is gpt.py")

#write code for  factorial

def factorial(n):   
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#driver fucntion
n = 5
print("Factorial of", n, "is", factorial(n))


#write code for  fibonacci series
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    #driver function
n = 10
print("Fibonacci series of", n, "is", fibonacci(n))

