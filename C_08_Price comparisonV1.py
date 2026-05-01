
def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")


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




# Main Routine goes here

# loop for testing purposes...
while True:
    print()

    item_name = []
    unit_costs = []

    # get user budget
    budget = num_check("Enter your budget: ")

    print("Enter items:")

    # item entry loop
    while True:
        name = not_blank("Item name: ")

        if name.lower() == "xxx":
            break

        price = num_check(f"Price for {name}: ")

        item_name.append(name)
        unit_costs.append(price)

        lowest = min(unit_costs)

    # check list is not empty
    if len(item_name) == 0:
        print("You must enter at least one item.\n")
        continue



    #Output lowest
    print(f"The lowest unit cost is {lowest:.2f}")

    if lowest <= budget:
        print("You can afford this item.\n")
    else:
        print("This item is over your budget.\n")

    # return function
