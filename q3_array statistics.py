# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================

# Function to calculate the sum
def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Function to calculate the average
def find_average(numbers):
    total = find_sum(numbers)
    return total / len(numbers)

# Function to find the maximum number
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Function to find the minimum number
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Main Program
n = int(input("How many numbers? "))

if n <= 0:
    print("Error: Number of values must be greater than 0.")
else:
    numbers = []

    # Read numbers into the list
    for i in range(n):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    # Display results
    print("\nResults:")
    print("Sum:    ", find_sum(numbers))
    print("Average:", find_average(numbers))
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))