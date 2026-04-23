# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")


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

ask_instructions = yes_no_check("would you like to see instructions? ")
if ask_instructions == "yes":
    instructions()
else:
    print('program continues')