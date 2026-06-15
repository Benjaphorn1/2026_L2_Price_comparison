
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name", "Unit Weight", "Item Cost", "Unit Cost"]

table.add_rows([
    ["A", 0.5, 8, 16.00],
    ["B", 0.45, 12, 26.67],
    ["C", 0.75, 15, 20.00]
])

print(table)