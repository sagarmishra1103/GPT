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
