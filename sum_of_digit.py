def sum_of_digits(number):
    digit_sum = 0
    number = abs(number)
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    return digit_sum
user_number = int(input("Enter a number: "))
result = sum_of_digits(user_number)
print(f"The sum of digits of {user_number} is {result}")