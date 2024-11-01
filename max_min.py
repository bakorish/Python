def find_max(num1, num2):
    return max(num1, num2)
def find_min(num1, num2):
    return min(num1, num2)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
max_value = find_max(num1, num2)
min_value = find_min(num1, num2)
print("Maximum between", num1, "and", num2, "is:", max_value)
print("Minimum between", num1, "and", num2, "is:", min_value)
