def power(base, exponent):
    return base ** exponent
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
result = power(base, exponent)
print(base, "raised to the power of", exponent, "is:", result)
