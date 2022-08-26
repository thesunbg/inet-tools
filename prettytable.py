import colorama

def printTable(table):
    # create a new list of 3 "0" values: one for each list in tableData
    colWidths = [0] * len(table)
    # search for the longest string in each list of tableData
    # and put the numbers of characters in the new list
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

    # "rotate" and print the list of lists
    for x in range(len(table)) :
        for y in range(len(table[0])) :
            print(colorama.Fore.LIGHTYELLOW_EX + table[x][y].rjust(colWidths[x]), end = ' ' * 10)
        print()
        x += 1

