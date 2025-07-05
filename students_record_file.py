from tabulate import tabulate
def showTable(lst):
    recording_table = [
    [' NAME ', ' AGE ', ' GENDER ', ' AVERAGE '],
    lst.append()]
    table = tabulate(recording_table, headers="firstrow")
    return print(tabulate(recording_table, tablefmt="grid"))
