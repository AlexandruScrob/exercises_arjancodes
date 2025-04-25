# F-strings

name = "Guido"
level = "advanced"
print(f"{name} is an {level} Python programmer!")

# Guido is an advanced Python programmer!

# Combine expressions directly:

age = 30
print(f"In 10 years, I will be {age + 10} years old.")

# Use f-strings to format numbers with precision or in human-readable formats.

pi = 3.14159
print(f"Pi rounded to two decimals: {pi:.2f}")

# Pi rounded to two decimals: 3.14

# Add thousands separators:

large_number = 123456789
print(f"Large number with commas: {large_number:,}")

# Display percentages:

success_rate = 0.874
print(f"Success rate: {success_rate:.1%}")

# Use f-strings with datetime objects for cleaner formatting.

from datetime import datetime

now = datetime.now()
print(f"Current date: {now:%Y-%m-%d}")
print(f"Current time: {now:%H:%M:%S}")

# Current date: 2024-12-17
# Current time: 11:13:32

# Align text for neatly formatted outputs:

name = "Python"
print(f"{name:<10} is left-aligned")  # Output: Python     is left-aligned
print(f"{name:>10} is right-aligned")  # Output:      Python is right-aligned
print(f"{name:^10} is centered")  # Output:   Python   is centered

# Python     is left-aligned
#     Python is right-aligned
#   Python   is centered

# Dynamic width formatting:

name = "Arjan"
width = 30
print(f"{name:^{width}}")

#             Arjan

# F-strings support a debugging syntax that displays both the expression and its result.

value = 42
print(f"{value=}")

value = 42
