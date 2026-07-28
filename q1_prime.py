
# Question 1: Check if a number is prime

# Step 1: Ask the user for input
num = int(input("Enter a number: "))

# Step 2: Handle small cases
if num <= 1:
    print(num, "is not a prime number")
else:
    # Step 3: Check divisibility
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # only check up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    
    # Step 4: Print result
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
# Question 1: Check if a number is prime

