def is_perfect(number):
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    return sum_divisors == number
def print_perfect_numbers(start, end):
    print("Perfect numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_perfect(num):
            print(num)
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))
print_perfect_numbers(start, end)
