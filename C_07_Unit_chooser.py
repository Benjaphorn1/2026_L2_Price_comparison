# the program will decide if the number entered
# is either grams or kilograms
def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")

def unit_chooser(question):
    """Calculates whether the weight is g or kg"""
    # Initialise variables and error message
    error = "Please enter a valid weight\n"

    valid = False
    while not valid:

        # ask user for weight...
        response = input(question)

        # check if second to last character is k...
        if response.endswith("kg"):
            weight_type = "kg"
            amount = response[:-2]

        elif response.endswith("g"):
            weight_type = "g"
            amount = response[:-1]

        else:
            weight_type = "unknown"
            amount = response

        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue


        except ValueError:
            print(error)
            continue

        if weight_type == "unknown" and amount >= 100:
            gram_type = yes_no_check(f"Do you mean {amount}g. y/n: ")

            # Set weight type base on user and answer above
            if gram_type == "yes":
                weight_type = "g"
            else:
                weight_type = "kg"

        elif weight_type == "unknown" and amount < 100:
            kilogram_type = yes_no_check(f"Do you mean {amount}kg?, y/n: ")
            if kilogram_type == "yes":
                weight_type = "kg"
            else:
                weight_type = "g"

        # convert grams to kg if the user enters grams
        if weight_type == "kg":
            return amount
        else:
            unit_weight = (amount/1000)
            return unit_weight


# looping for testing
while True:
    thing = unit_chooser("What is the weight? ")
    print(f"You put {thing}kg")
    print()



