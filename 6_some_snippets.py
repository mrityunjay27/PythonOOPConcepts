# 1. List compression
numbers = [1, 2, 3, 4]
# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

# 2. List compression
# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0]
print(even_numbers)

# 3. List compression
word = "Python"
vowels = "aeiou"
# find vowel in the string "Python"
result = [char for char in word if char in vowels]
print(result)

# 4. Lambda / Anonymous function
# lambda that accepts one argument
greet_user = lambda name: print('Hey there,', name)

# lambda call
greet_user('Delilah')

# Output: Hey there, Delilah
