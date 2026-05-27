# Functions go here
def comparison_function(lst):
    """Finds and returns the cheapest item (price and name) from a list of (name, price)"""
    # Set starting values using the first item in the list
    lowest_price = lst[0][1]
    cheapest_item_name = lst[0][0]
    # Check if the current item's price is cheaper than the lowest so far
    for item in lst:
        if item[1] < lowest_price:
            lowest_price = item[1]
            cheapest_item_name = item[0]
    # Return the cheapest price and its name
    return lowest_price, cheapest_item_name


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
# ask user for budget
budget = num_check("What is the budget? ")

# loop for testing purposes...
while True:
    print()

    items = []


    print("-Enter items-")

    # item entry loop
    while True:
        name = not_blank("Item name: ")

        if name.lower() == "xxx":
            break

        price = num_check(f"Price for {name}: ")

        items.append((name, price))

    # check list is not empty
    if len(items) == 0:
        print("You must enter at least one item.\n")
        continue


    # return function
    cheapest_price, cheapest_name = comparison_function(items)

    # if the cheapest item is higher than the budget output message
    if cheapest_price > budget:
        print()
        print("Nothing is within your budget")
        print(f"But Item {cheapest_name} is the cheapest at {cheapest_price}")

    # output results
    else:
        print(f"\nCheapest item is {cheapest_name} at ${cheapest_price:.2f}")
