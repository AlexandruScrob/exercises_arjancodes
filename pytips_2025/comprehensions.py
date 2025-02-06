# Generating squares of even numbers:

squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)

# Mapping numbers to their cubes:

cubes = {x: x**3 for x in range(5)}
print(cubes)

# Unique lengths of words:

words = ["hello", "world", "python", "hello"]
unique_lengths = {len(word) for word in words}
print(unique_lengths)  # Output: {5, 6}

# Generators look like list comprehensions but use parentheses. They compute values lazily, making them memory-efficient.

squares_gen = (x**2 for x in range(5))
for square in squares_gen:
    print(square)

# Comprehensions can be nested for multi-dimensional data processing.

# Flattening a 2D list:
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)
