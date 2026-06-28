import pandas
from tabulate import tabulate
from datetime import date


def make_statement(statement, decoration):
    """emphasises headings by adding decoration
    at the start and end"""
    #create the string and return it
    heading = f"{decoration * 3} {statement} {decoration * 3}"
    return heading


def not_blank(question):
    """checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def yes_no_check(question):
    """checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes or no ")


def num_check(question, exit_code=None):
    """checks that response is a float more than zero"""

    error = "Please enter a number more than 0."

    while True:
        response = input(question)

        # exit code check
        if response == exit_code:
            return response

        try:
            response = float(response)

            if response > 0:
                return response

            print(error)

        except ValueError:
            print(error)


def instructions():
    """displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''This program will ask you for... 
    - Your total budget
    - The names of your products
    - The weight of your product in g/kg or ml/l
    - Get the cost of that product

Please make sure that you enter the abbreviation of the unit for 
example: kg - kilogram, l - litres, g - grams, ml - millilitre

If you do not enter a unit for the weight the program will ask if 
it grams or kilogram depending on the number value.

If any items you enter are not within the budget the program will 
you but will still output the cheapest item

Finally it will tell you the recommended product to get and its 
value. 

To exit the program use the exit code 'xxx' in the item name

The data will also be written to a text file which has the 
same name as today's date and your chosen file name.

    ''')


def get_input(question):
    """gets number and detects unit if its entered"""

    while True:

        response = input(question).lower().strip()
        response = response.replace(" ", "")

        #kilograms
        if response.endswith("kg"):
            unit_input = "kg"
            amount_input = response[:-2]

        #grams
        elif response.endswith("g"):
            unit_input = "g"
            amount_input = response[:-1]

        #millilitres
        elif response.endswith("ml"):
            unit_input = "ml"
            amount_input = response[:-2]

        #litres
        elif response.endswith("l"):
            unit_input = "l"
            amount_input = response[:-1]

        #no unit entered
        else:
            print("Unknown unit please use kg, g, l, or ml")
            unit_input = "unknown"
            amount_input = response

        #check amount is a valid input
        try:
            amount_input = float(amount_input)

            if amount_input <= 0:
                print("Amount must be more than 0")
                continue

            #send values back to main routine
            return amount_input, unit_input

        except ValueError:
            print("Please enter a valid amount")


def unit_pick(weight_value):
    """Decides unit if user didn't enter one"""

    #large amount above 100 asked if g or ml
    if weight_value > 100:

        while True:
            unit_response = input("Is this grams g or millilitres ml? ").lower()

            if unit_response in ["g", "grams"]:
                return "g"

            elif unit_response in ["ml", "millilitres"]:
                return "ml"

            else:
                print("Please enter g or ml")

    #smaller values asked if kg or l
    else:

        while True:
            unit_response = input("Is this kilograms kg or litres L? ").lower()

            if unit_response in ["kg", "kilograms"]:
                return "kg"

            elif unit_response in ["l", "litres"]:
                return "l"

            else:
                print("Please enter kg or L")


def convert_units(value, unit_type):
    """Converts everything to kg or L"""

    # if unit is g divide by 1000 for kg
    if unit_type == "g":
        return value / 1000, "kg"

    # if unit is ml divide by 1000 for l
    elif unit_type == "ml":
        return value / 1000, "l"

    # return value if kg
    elif unit_type == "kg":
        return value, "kg"

    # return value if l
    elif unit_type == "l":
        return value, "l"


def comparison_function(lst):
    """Finds and returns the cheapest item (price and name) from a list of (name, price)"""
    #set starting values using the first item in the list
    lowest_price = lst[0][1]
    cheapest_item_name = lst[0][0]
    #check if the current item's price is cheaper than the lowest so far
    for current_item in lst:
        if current_item[1] < lowest_price:
            lowest_price = current_item[1]
            cheapest_item_name = current_item[0]
    #return the cheapest price and its name
    return lowest_price, cheapest_item_name


def format_currency(value):
    """format a number into a dollar currency specifically"""
    return f"${value:.2f}"


def format_weight(value):
    """format a number to 2 decimal places for weight/volume"""
    return f"{value:.2f}"


#main routine goes here

#lists
all_names = []
all_weight = []
all_final_units = []
all_costs = []
all_unit_costs = []
names_unit_costs = []

print(make_statement("Price Comparison Calculator", "💲"))

#print instructions if user says yes
print()
want_instructions = yes_no_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

budget = num_check("What is the budget? ")
print()

file_name = not_blank("File name: ")
print()

#main routine loop
while True:

    item_name = not_blank("Item name: ")

    #exit code
    if item_name == "xxx":
        break

    #get item amount and unit
    amount, unit = get_input("Item weight or volume: ")

    #ask user for unit if not entered
    if unit == "unknown":
        unit = unit_pick(amount)

    #convert units to kg/L if needed
    item_weight, new_unit = convert_units(amount, unit)
    # Get item cost
    item_cost = num_check("Item cost: $", "xxx")

    #Calculate unit cost
    unit_cost = item_cost / item_weight

    # display item info
    print(f"{item_name}: {item_weight:.2f}{new_unit}")
    print(f"Unit cost: ${unit_cost:.2f} per {new_unit}")
    print()

    #ddd inputs to lists
    all_names.append(item_name)
    all_weight.append(item_weight)
    all_final_units.append(new_unit)
    all_costs.append(item_cost)
    all_unit_costs.append(unit_cost)
    #add names and unit cost to one list for comparison
    names_unit_costs.append((item_name, unit_cost))

#check that at least one item entered
if len(all_names) == 0:
    print("You need to enter at least one item.")
else:
    cheapest_price, cheapest_name = comparison_function(names_unit_costs)

    #get position of cheapest item in lists
    item_price_position = all_names.index(cheapest_name)

    #get the original cost using that position
    item_price = all_costs[item_price_position]

    #variable for table to prevent error
    weight_colm = "Unit Weight/Vol"

    #pandas output dictionary setup
    price_calc_dict = {
        "Name": all_names,
        weight_colm : all_weight,
        "Unit": all_final_units,
        "Item costs": all_costs,
        "Unit Costs": all_unit_costs,
    }

    #convert to Dataframe format numbers to currency and print table
    calc_frame = pandas.DataFrame(price_calc_dict)

    calc_frame[weight_colm] = calc_frame[weight_colm].apply(format_weight)
    calc_frame["Item costs"] = calc_frame["Item costs"].apply(format_currency)
    calc_frame["Unit Costs"] = calc_frame["Unit Costs"].apply(format_currency)

    expense_string = tabulate(
        calc_frame, headers="keys", tablefmt="grid", showindex=False
    )

    #get date for heading and filename
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    main_heading = make_statement(
        f"Price Comparison Calculator ({day}/{month}/{year})", "="
    )
    results_heading = make_statement("Results", "=")
    budget_string = f"Your budget is ${budget:.2f}\n"

    recommendation_heading = make_statement(
        "Recommendation", "="
    )

    # if the lowest item brice is above the budget print recommendation and error
    if item_price > budget:
        recommendation_string = (
            f"Nothing is within your budget\n"
            f"Cheapest item: {cheapest_name}\n"
            f"Unit price: ${cheapest_price:.2f}\n"
            f"Item price: ${item_price:.2f}"
        )
    # if under budget print recommendation
    else:
        recommendation_string = (
            f"Recommended item: {cheapest_name}\n"
            f"Unit price: ${cheapest_price:.2f}\n"
            f"Item price: ${item_price:.2f}"
        )

    # print outputs for write to file
    to_write = [
        main_heading,
        results_heading,
        budget_string,
        expense_string,
        "\n",
        recommendation_heading,
        recommendation_string,
    ]

    print()
    for item in to_write:
        print(item)

    #create filename
    file_name = f"{file_name}_{year}_{month}_{day}"
    write_to = "{}.txt".format(file_name)

    #create file
    text_file = open(write_to, "w+")

    #write items to file
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

    text_file.close()
