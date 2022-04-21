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
        allPaths.append(path + [matrix[row][coloumn]])
        return 

    # include the current cell in the path
    path.append(matrix[row][coloumn])
    # move right
    if row < rows-1 and coloumn + 1 < coloumns:
        print(row,coloumn)
        getPaths(matrix, path, row, coloumn + 1)
 
    # move down
    if 0 <= row + 1 < rows and 0 <= coloumn < coloumns:
        getPaths(matrix, path, row + 1, coloumn)
 
    # backtrack: remove the current cell from the path
    path.pop()


matrix = [
    [1, 2, 3,],
    [4, 5, 6],
    [7, 8, 9]
]

path = []
getPaths(matrix, path)
print(allPaths)