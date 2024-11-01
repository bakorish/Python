def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number to find its factorial: "))

# Call the function to find factorial
result = factorial(num)

# Print the result
print("Factorial of", num, "is:", result)
