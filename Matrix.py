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

allPaths = []
def getPaths(matrix, path, row=0, coloumn=0):
 
    # base case
    if not matrix or not len(matrix):
        return
 
    rows = len(matrix) 
    coloumns = len(matrix[0])
 
     # if the last cell is reached, print the route
    if row == rows - 1 and coloumn == coloumns - 1:
        global allPaths
        allPaths.append(path + [row,coloumn])
        return 

    # include the current cell in the path
    path.append([row,coloumn])
    # move right
    if 0 <= row < rows and 0 <= coloumn + 1 < coloumns:
        getPaths(matrix, path, row, coloumn + 1)
 
    # move down
    if 0 <= row + 1 < rows and 0 <= coloumn < coloumns:
        getPaths(matrix, path, row + 1, coloumn)
 
    # backtrack: remove the current cell from the path
    path.pop()


matrix = [
    [1, 2, 3,243],
    [4, 5, 6,234],
    [7, 8, 9,235],
    [23,454,2,123]
]

path = []
getPaths(matrix, path)
print(allPaths)