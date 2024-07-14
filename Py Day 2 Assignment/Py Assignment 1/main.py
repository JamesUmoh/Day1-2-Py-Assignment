def sum_of_digits(number):
    # Extract the tens and units place digits
    tens = number // 10
    units = number % 10

    # Calculate the sum of the digits
    digit_sum = tens + units

    # Return the result
    return f"{tens} + {units} = {digit_sum}"

# Example usage
input_number = int(input("Enter a two-digit number: "))
result = sum_of_digits(input_number)
print(result)


input_number = int(input("Enter a two-digit number: "))

# Extract the tens and units place digits
tens = input_number // 10
units = input_number % 10

# Calculate the sum of the digits
digit_sum = tens + units

# Return the result
def sum_of_digits(number):
    return f"{digit_sum}"
    # return f"{tens} + {units} = {digit_sum}"

result = sum_of_digits(input_number)
print(result)

