from tabulate import tabulate
def showTable(lst: list):
    table = lst
    headers = ['NAME', 'AGE', 'GENDER', 'AVERAGE']
    print(tabulate(table, headers, tablefmt="fancy_grid", stralign='center', numalign='center', floatfmt=".1f"))
