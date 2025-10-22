import math

# Ask the user for a number
try:
    number = float(input("Enter a number: "))

    # Calculate values using math module
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    # Display results
    print(f"Square root of {number} is: {square_root}")
    print(f"Natural log (base e) of {number} is: {natural_log}")
    print(f"Sine of {number} radians is: {sine_value}")

except ValueError:
    print("Please enter a valid positive number.")
except Exception as e:
    print(f"An error occurred: {e}")
