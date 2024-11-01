def sum_of_series(n):
    total_sum =0
    term = 7
    for i in range(n):
        total_sum += term
        term += 13 + (i * 7)
    return total_sum
n = 100
result = sum_of_series(n)
print("Sum of the series up to", n, "terms:", result)
