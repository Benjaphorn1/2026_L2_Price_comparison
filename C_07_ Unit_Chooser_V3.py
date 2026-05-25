# Checks that the user enters yes / no
def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes or no ")

# Gets number and detects unit if its entered
def get_input(question):

    while True:

        response = input(question).lower().strip()

        # kilograms
        if response.endswith("kg"):
            unit = "kg"
            amount = response[:-2]

        # grams
        elif response.endswith("g"):
            unit = "g"
            amount = response[:-1]

        # millilitres
        elif response.endswith("ml"):
            unit = "ml"
            amount = response[:-2]

        # litres
        elif response.endswith("l"):
            unit = "l"
            amount = response[:-1]

        # no unit entered
        else:
            unit = "unknown"
            amount = response

        # Check amount is a valid input
        try:
            amount = float(amount)

            if amount <= 0:
                print("Amount must be more than 0")
                continue

            # send values back to main routine
            return amount, unit

        except ValueError:
            print("Please enter a valid amount")

# Decides unit if user didn't enter one
def unit_pick(amount):

    # Large values above 100 asked if g or ml
    if amount > 100:

        while True:
            response = input("Is this grams g or millilitres ml? ").lower()

            if response in ["g", "grams"]:
                return "g"

            elif response in ["ml", "millilitres"]:
                return "ml"

            else:
                print("Please enter g or ml")

    # Smaller values asked if kg or l
    else:

        while True:
            response = input("Is this kilograms kg or litres L? ").lower()

            if response in ["kg", "kilograms"]:
                return "kg"

            elif response in ["l", "litres"]:
                return "l"

            else:
                print("Please enter kg or L")

# Converts everything to kg or L
def convert_units(amount, unit):

    if unit == "g":
        return amount / 1000, "kg"

    elif unit == "ml":
        return amount / 1000, "L"

    elif unit == "kg":
        return amount, "kg"

    elif unit == "l":
        return amount, "L"

# Main routine
while True:

    # Get amount and unit from function
    amount, unit = get_input("Enter amount: ")

    # Ask user for unit if not entered
    if unit == "unknown":
        unit = unit_pick(amount)

    # Convert units
    converted, new_unit = convert_units(amount, unit)

    # Display result
    print(f"Converted Unit {converted}{new_unit}")
    print()



