
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print ( arr[i][j], end=" "),
        print (" ")

def check_if_number_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False            

def check_if_number_in_column(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


def check_if_number_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True         
    return False


def findemptylocation(arr, l):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def check_if_number_fits(grid, num, row, col):
    return (not check_if_number_in_box(grid, row - row%3, col - col %3, num) 
            and not check_if_number_in_row(grid, row, num)
            and not check_if_number_in_column(grid,col,num))

#print(check_if_number_fits(grid,num,row,col))
#print([print(i) for i in range(9)])

def solvesodoku(grid):

    l = [0,0]

    if (not findemptylocation(grid, l)):
        return True
    
    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if (check_if_number_fits(grid, num, row, col)):
            
            grid[row][col] = num

            if(solvesodoku(grid)):
                return True

            grid[row][col] = 0

    return False 

if __name__ == "__main__":

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    print_grid(grid)
    print("\n")


    if solvesodoku(grid):
        print_grid(grid)

    else: print( "No Solution Exists" ) 
