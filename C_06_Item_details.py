


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

def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes or no ")



def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


def unit_chooser(item_weight):
    """Calculates whether the weight is g or kg"""
    # Initialise variables and error message
    error = "Please enter a valid weight\n"

    valid = False
    while not valid:

        # ask user for weight...
        response = input("What is the weight? (200g or 0.2kg): ").lower().strip()

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


#Main routine goes here
# lists for panda
all_names = []
all_weight = []
all_costs = []
all_grams = []
all_unit_costs = []

budget = num_check("What is the budget? ")
while True:

    item_name = not_blank("Item name: ")

    if item_name == "xxx":
        break

    item_weight = unit_chooser("Item weight: ")
    item_cost = num_check("Item cost: $", "float")

    unit_cost = item_cost / item_weight
    grams = item_weight * 1000

    print(f"{item_name}: {grams:.0f}g ({item_weight:.2f}kg)")
    print(f"Unit cost: ${unit_cost:.2f} per kg")
    print()

    all_names.append(item_name)
    all_weight.append(item_weight)
    all_grams.append(grams)
    all_costs.append(item_cost)
    all_unit_costs.append(unit_cost)


print(f"Your budget is ${budget}.")
print("name", all_names,
  ",Kg", all_weight,
  ",costs", all_costs,
  ",grams", all_grams,
  ",unit costs", all_unit_costs)

# Find the lowest unit cost
lowest = min(all_unit_costs)

# Find the index (position) of that lowest cost
lowest_index = all_unit_costs.index(lowest)

# Use the index to get the corresponding item name
best_item = all_names[lowest_index]

print(f"\n--- Results ---")
print(f"Your budget is ${budget:.2f}")
print(f"The lowest unit cost is ${lowest:.2f} per kg")
print(f"This is for: {best_item}")

lowest = min(all_unit_costs)
print(f"This is the lowest {lowest:.2f}")

