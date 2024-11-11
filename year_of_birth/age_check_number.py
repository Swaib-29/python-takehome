# Program to greet the user, calculate their birth year, and analyze their favorite number.
# This script prompts the user for their name, age, and favorite number.
# It calculates their birth year, checks if their favorite number is even or odd,
# and gives additional feedback based on the favorite number's value.

# Get the user's name
name = input("Please enter your name: ")
print(f"Hello, {name}! Welcome!")

# Ask  the user to enter age and then calculate  year he was born
while True:
    try:
        age = int(input("Please enter your age: "))  # Convert input to integer
        current_year = 2024
        birth_year = current_year - age
        print(f"{name}, you were born in {birth_year}.")
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a numeric value for your age.")  # catch the  Error message for non-numeric input

# Ask the user for their favorite number and determine if it's even or odd
while True:
    try:
        favorite_number = int(input("Please enter your favorite number: "))
        
        # Check if the number is even or odd
        if favorite_number % 2 == 0:
            print("Your favorite number is even.")
        else:
            print("Your favorite number is odd.")
        
        # Chained and nested conditionals based on the value of the favorite number
        if favorite_number > 10:
            print("That's a big number!")
            if favorite_number > 100:
                print("Wow, you like really large numbers!")
        elif favorite_number < 10:
            print("That's a small number!")
        else:
            print("10 is a great choice!")
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a numeric value for your favorite number.")  # Error message for non-numeric input