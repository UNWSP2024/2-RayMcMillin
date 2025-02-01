
def average_age():
    # Get User Input
    age1 = int(input("Enter the age of friend 1: "))
    age2 = int(input("Enter the age of friend 2: "))
    age3 = int(input("Enter the age of friend 3: "))
    age4 = int(input("Enter the age of friend 4: "))
    age5 = int(input("Enter the age of friend 5: "))

    # Sum ages
    total_age = age1 + age2 + age3 + age4 + age5
    # Average the ages
    average_age = total_age / 5
    # Print the results
    print("The average age is:", average_age)
# Line which calls the above function.
average_age()
