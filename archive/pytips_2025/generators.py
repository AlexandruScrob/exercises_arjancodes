# A generator function that yields square numbers
def square_numbers(limit: int):
    for n in range(limit):
        yield n * n


# Use the generator function to compute values
for square in square_numbers(5):
    print(square)

# 0
# 1
# 4
# 9
# 16

# Generators compute values lazily, meaning they only produce results when explicitly requested.

import time


# A generator that computes the square of numbers with a delay
def delayed_squares(limit):
    for n in range(limit):
        print(f"Computing square for: {n}")
        time.sleep(1)  # Simulate a delay in computation
        yield n * n


# Instantiate the generator
gen = delayed_squares(3)

# Step through the generator manually
print("Fetching values on the fly:")
print(next(gen))  # Compute square of 0
print(next(gen))  # Compute square of 1
print(next(gen))  # Compute square of 2

# Fetching values on the fly:
# Computing square for: 0
# 0
# Computing square for: 1
# 1
# Computing square for: 2
# 4
