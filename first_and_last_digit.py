def find_first_and_last_digit(number):
    number_str = str(number)
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    return first_digit, last_digit
number = int(input("Enter a number: "))
first_digit, last_digit = find_first_and_last_digit(number)
print("First digit:", first_digit)
print("Last digit:", last_digit)
