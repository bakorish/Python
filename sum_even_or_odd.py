def sum_even_or_odd(start, end, is_even=True):
    sum_numbers = 0
    for num in range(start, end + 1):
        if is_even and num % 2 == 0:
            sum_numbers += num
        elif not is_even and num % 2 != 0:
            sum_numbers += num
    return sum_numbers
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
choice = input("Enter 'even' or 'odd' to find the sum of even or odd numbers: ").lower()
if choice == 'even':
    result = sum_even_or_odd(start, end, is_even=True)
    print("Sum of even numbers between", start, "and", end, "is:", result)
elif choice == 'odd':
    result = sum_even_or_odd(start, end, is_even=False)
    print("Sum of odd numbers between", start, "and", end, "is:", result)
else:
    print("Invalid choice! Please enter 'even' or 'odd'.")
