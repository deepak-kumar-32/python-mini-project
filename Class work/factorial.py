n = int(input("Enter a number to calculate its factorial: "))
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1) 
result = factorial(n)
print(f"The factorial of {n} is: {result}") 