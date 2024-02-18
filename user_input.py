# Ask the user for their name and store it in the variable "name"
name = str(input("What is your name? "))

# Ask the user for their age and store it in the variable "age"
age = int(input("How old are you? "))

# Ask the user for their location and store it in the variable "location"
location = str(input("Where do you live? "))

# Print out a personalized message using the user's name, age, and location
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))
