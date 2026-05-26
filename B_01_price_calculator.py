def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes or no ")

def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code and return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''This program will ask you for... 
    - Your total budget
    - The names of your products
    - The weight of your product in grams/kilograms
    - Get the cost of that product

If you do not enter a unit for the weight the program will ask if 
it grams or kilogram depending on the number value.

The program might ask if you are willing to go over the budget or
not.

Finally it will tell you the recommended product to get and its 
value. 

To exit the program use the exit code 'xxx'

The data will also be written to a text file which has the 
same name as today's date and your chosen file name.

    ''')

def get_input(question):
    """Gets number and detects unit if its entered"""

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

def unit_pick(amount):
    """Decides unit if user didn't enter one"""

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

def convert_units(amount, unit):
    """Converts everything to kg or L"""

    if unit == "g":
        return amount / 1000, "kg"

    elif unit == "ml":
        return amount / 1000, "L"

    elif unit == "kg":
        return amount, "kg"

    elif unit == "l":
        return amount, "L"

# Main routine goes here

# lists for panda
all_names = []
all_weight = []
all_costs = []
all_grams = []
all_unit_costs = []

make_statement("Price Comparison Calculator", "💲")

# Print instructions if user says yes
print()
want_instructions = yes_no_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

budget = num_check("What is the budget? ")

# Main Routine loop
while True:

    item_name = not_blank("Item name: ")

    # Exit code
    if item_name == "xxx":
        break

    # Get item amount and unit
    amount, unit = get_input("Item weight or volume: ")

    # Ask user for unit if not entered
    if unit == "unknown":
        unit = unit_pick(amount)

    # Convert units to kg / L
    item_weight, new_unit = convert_units(amount, unit)

    # Get item cost
    item_cost = num_check("Item cost: $", "float")


    # Calculate unit cost
    unit_cost = item_cost / item_weight

    # Display item info
    print(f"{item_name}: {item_weight:.2f}{new_unit}")
    print(f"Unit cost: ${unit_cost:.2f} per {new_unit}")
    print()

    # Add data to lists
    all_names.append(item_name)
    all_weight.append(item_weight)
    all_costs.append(item_cost)
    all_unit_costs.append(unit_cost)

# Check at least one item entered
if len(all_names) == 0:
    print("You need to enter at least one item.")

else:

# Output results
    make_statement("results","=")
    print(f"Your budget is ${budget:.2f}")

    print(f"name - {all_names}")
    print(f"Kg/L - {all_weight}")
    print(f"costs - {all_costs}")
    print(f"unit costs - {all_unit_costs}")

    # # Find lowest unit cost
    # lowest = min(all_unit_costs)
    #
    # # Find index of lowest cost item
    # best_index = all_unit_costs.index(lowest)
    #
    # # Get best item name
    # best_item = all_names[best_index]
    #
    # print()
    # print(f"Best value item: {best_item}")
    # print(f"Unit cost: ${lowest:.2f} per kg/L")