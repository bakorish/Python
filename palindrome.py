def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
n = 69696
result = is_palindrome(n)
if result:
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")
