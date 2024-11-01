def sum_of_first_and_last_digit(number):
    res = number % 10
    while number > 9:
        number //= 10
        res += number
    return res
n = 6900
result = sum_of_first_and_last_digit(n)
print(f"Addition of first and last digit of the number is {result}")
