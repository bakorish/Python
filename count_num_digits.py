def count_digits(number):
    number_str = str(number)
    num_digits = len(number_str)
    return num_digits
number = int(input("enter a number: "))
num_digits = count_digits(number)
print("Number of digits:", num_digits)
