def product_of_digits(number):
    number_str = str(number)
    product = 1
    for digit_char in number_str:
        digit = int(digit_char)
        product *= digit
    return product
number = int(input("Enter a number: "))
result = product_of_digits(number)
print("Product of digits:", result)
 