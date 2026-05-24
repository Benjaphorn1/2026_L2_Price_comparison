# Checks that the user enters yes / no
def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        # Ask user for response and make lowercase
        response = input(question).lower()

        # Check for yes responses
        if response in ["y", "yes"]:
            return "yes"

        # Check for no responses
        elif response in ["n", "no"]:
            return "no"

        # If response is invalid
        print("Please answer yes / no (y / n)")


# Determines whether the user entered grams, litres, or items
def unit_chooser(question):
    """Chooses which unit the user enters and Converts units into standard form"""

    # Error message
    error = "Please enter a valid amount\n"

    while True:

        # Ask user for input
        response = input(question).lower()

        # weight
        # Check if input ends with kg
        if response.endswith("kg"):
            unit_type = "kg"
            amount = response[:-2]

        # Check if input ends with g
        elif response.endswith("g"):
            unit_type = "g"
            amount = response[:-1]

        # Volume
        # Check if input ends with litres
        elif response.endswith("l"):
            unit_type = "l"
            amount = response[:-1]

        # Check if input ends with millilitres
        elif response.endswith("ml"):
            unit_type = "ml"
            amount = response[:-2]

        # If no unit was entered
        else:
            unit_type = "unknown"
            amount = response

        # Check amount is a valid number
        try:
            amount = float(amount)

            # Number must be more than 0
            if amount <= 0:
                print(error)
                continue

        # If amount is not a number
        except ValueError:
            print(error)
            continue

        # If the unit is unknown, ask user what they meant
        if unit_type == "unknown":

            print("\nWhat unit did you mean?")
            print('1. grams/kilograms ')
            print('2. millilitres/litres ')

            # Ask user to choose a unit type
            choice = input("\nChoose 1 or 2: ")

            # weight
            if choice == "1":

                # Ask whether user meant kilograms
                gram_type = yes_no_check(
                    f"Do you mean {amount}kg? y/n: ")

                # Set unit type based on response
                if gram_type == "yes":
                    unit_type = "kg"
                else:
                    unit_type = "g"

            # Volume
            elif choice == "2":

                # Ask whether user meant litres
                litre_type = yes_no_check(
                    f"Do you mean {amount}L? y/n: ")

                # Set unit type based on response
                if litre_type == "yes":
                    unit_type = "l"
                else:
                    unit_type = "ml"

            # Invalid choice
            else:
                print(error)
                continue


        # Convert everything into standard units

        # Weight stays as kilograms
        if unit_type == "kg":
            return amount, "kg"

        # Convert grams to kilograms
        elif unit_type == "g":
            return amount / 1000, "kg"

        # Volume stays as litres
        elif unit_type == "l":
            return amount, "L"

        # Convert millilitres to litres
        elif unit_type == "ml":
            return amount / 1000, "L"


# Main routine for testing
while True:

    # Call function and store returned values
    result, unit = unit_chooser("Enter amount: ")

    # Output converted amount
    print(f"\nUnit amount: {result} {unit}")
    print()