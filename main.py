# Exercise 1

# Create a list named students containing some student names (strings).
from turtle import home


students = ['Ivan', 'Kobe', 'Tony', 'Nipsey']
# Print out the second student's name.
print(students[1])
# Print out the last student's name.
print(students[-1])

# Exercise 2

# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
foods = ('burgers', 'kbbq', 'tacos', 'shrimp')
# Use a for loop to print out the string "food goes here is a good food".
for food in foods:
    print(f'{food} is a good food')

# Exercise 3

# Using a for loop, print just the last two food strings from foods.
for food in foods:
    print(foods[-2:])

# Exercise 4

# Create a dictionary named home_town containing the keys of city, state and population.
home_town = {
    'City': 'Los Angeles',
    'State': 'California',
    'Population': '12345'
}

# Print a string with this format:
for key, val in home_town.items():
    print(f'I ')

# "I was born in city, state - population of population"

# Exercise 5

# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

# Exercise 6

# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }

# Iterate over cohort printing out each element.

# Exercise 7

# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

# Exercise 8

# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
