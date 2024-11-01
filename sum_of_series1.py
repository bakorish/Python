def sum_of_series(n):
    total_sum = 0
    term = 5
    sign = 1
    for i in range(n):
        total_sum += sign * term
        term += 6
        sign *= -1
    return total_sum
n = 75
result = sum_of_series(n)
print("Sum of the series up to", n, "terms:", result)
