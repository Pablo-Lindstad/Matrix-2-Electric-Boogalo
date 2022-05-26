function minSum(list)
    rows = length(list)
    coloumns = length(list[1])
    for row in 1:rows
      for coloumn in 1:coloumns
        if row == 1 && coloumn == 1
        elseif row == 1
          list[row][coloumn] += list[row][coloumn-1]
        elseif coloumn == 1
          list[row][coloumn] += list[row-1][coloumn]
        else
          if list[row-1][coloumn] < list[row][coloumn-1]
            list[row][coloumn] += list[row-1][coloumn]
          else
            list[row][coloumn] += list[row][coloumn-1]
          end
        end
      end
    end
    return (list[rows][coloumns])
  end
  
  function maxSum(list)
    rows = length(list)
    coloumns = length(list[1])
    for row in 1:rows
      for coloumn in 1:coloumns
        if row == 1 && coloumn == 1
        elseif row == 1
          list[row][coloumn] += list[row][coloumn-1]
        elseif coloumn == 1
          list[row][coloumn] += list[row-1][coloumn]
        else
          if list[row-1][coloumn] > list[row][coloumn-1]
            list[row][coloumn] += list[row-1][coloumn]
          else
            list[row][coloumn] += list[row][coloumn-1]
          end
        end
      end
    end
    return (list[rows][coloumns])
  end