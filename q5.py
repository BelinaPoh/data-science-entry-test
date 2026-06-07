"""
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
"""
def check_divisibility(num, divisor):
	# Make sure num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
    	raise TypeError("num and divisor are not numeric")
    # Return True if num is divisible by divisor
    elif num % divisor == 0:
    	return True
    # Return False if num is not divisible by divisor
    else:
        return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
