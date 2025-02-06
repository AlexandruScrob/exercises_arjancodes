# You can use enumerate to loop through an iterable while keeping track of the index

items = ["apple", "banana", "cherry"]
for index, item in enumerate(items, start=1):
    print(f"{index}: {item}")

# Then there’s zip, which combines two or more iterables element-wise, creating tuples:

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# any and all are also quite useful:

numbers = [1, 0, 3, 0]
print(any(numbers))  # Output: True (at least one non-zero)
print(all(numbers))  # Output: False (not all are non-zero)

# True
# False
#
# map transforms an iterable by applying a function to each element:

numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))

# [1, 4, 9, 16]

# Use filter to select elements based on a condition:

numbers = [10, 15, 20, 25, 30]
divisible_by_10 = filter(lambda x: x % 10 == 0, numbers)
print(list(divisible_by_10))

# Use reversed to reverse an iterable without modifying it.

items = ["apple", "banana", "cherry"]
for item in reversed(items):
    print(item)

# cherry
# banana
# apple
#
# Did you know min and max also work with custom keys?

words = ["apple", "banana", "cherry"]
longest_word = max(words, key=len)
print(f"The longest word is {longest_word} with {len(longest_word)} characters.")

# The longest word is banana with 6 characters.
