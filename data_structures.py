# Set Comprehensions Example
# Create a set of squares of numbers from 1 to 10
squares_set = {x ** 2 for x in range(1, 11)}
print("Set of squares from 1 to 10:", squares_set)

# Filter even squares using set comprehension
even_squares_set = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print("Set of even squares:", even_squares_set)

# zip() Function Example
# Combine two lists into a list of tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print("Combined list using zip():", combined)

# Unzip the combined list
unzipped_names, unzipped_ages = zip(*combined)
print("Unzipped names:", unzipped_names)
print("Unzipped ages:", unzipped_ages)