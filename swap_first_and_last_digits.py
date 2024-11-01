def swap_first_and_last_digits(number):
    number_str = str(number)
    
    # Check if the number has more than one digit
    if len(number_str) > 1:
        swapped_number_str = number_str[-1] + number_str[1:-1] + number_str[0]
        swapped_number = int(swapped_number_str)
        return swapped_number
    else:
        return number
number = int(input("Enter a number: "))
swapped_number = swap_first_and_last_digits(number)
print("Number after swapping first and last digits:", swapped_number)

