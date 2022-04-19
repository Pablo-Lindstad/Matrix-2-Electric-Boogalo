def maxSum(list):
    rows = len(list)
    coloumns = len(list[0])
    for row in range(0,rows):
        for coloumn in range(0,coloumns):
            if row == 0 and coloumn == 0:
                pass
            elif row == 0:
                list[row][coloumn] += list[row][coloumn-1]
            elif coloumn == 0:
                list[row][coloumn] += list[row-1][coloumn]
            else:
                if list[row-1][coloumn] > list[row][coloumn-1]: 
                    list[row][coloumn] += list[row-1][coloumn]
                else:
                    list[row][coloumn] += list[row][coloumn-1]
    return(list[rows-1][coloumns-1])

def minSum(list):
    rows = len(list)
    coloumns = len(list[0])
    for row in range(0,rows):
        for coloumn in range(0,coloumns):
            if row == 0 and coloumn == 0:
                pass
            elif row == 0:
                list[row][coloumn] += list[row][coloumn-1]
            elif coloumn == 0:
                list[row][coloumn] += list[row-1][coloumn]
            else:
                if list[row-1][coloumn] < list[row][coloumn-1]:
                    list[row][coloumn] += list[row-1][coloumn]
                else:
                    list[row][coloumn] += list[row][coloumn-1]
    return(list[rows-1][coloumns-1])