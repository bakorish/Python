def reverse_number(number):
    original_number = number
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    print(f"Original Number: {original_number}")
    print(f"Reversed Number: {reversed_num}")
n = 96578
reverse_number(n)