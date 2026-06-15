import pandas
from tabulate import tabulate

data = [
    ["A", 0.5, 8, 16.00],
    ["B", 0.45, 12, 26.67],
    ["C", 0.75, 15, 20.00]
]

headers = ["Name", "Unit Weight", "Item Cost", "Unit Cost"]

print(tabulate(data, headers=headers, tablefmt="grid"))