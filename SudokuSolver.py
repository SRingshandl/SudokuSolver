import pandas

grid_original = [[9,6,2,0,7,8,5,0,0],
                 [1,0,5,0,0,9,3,0,0],
                 [3,0,0,0,0,0,8,2,0],
                 [0,0,1,0,0,0,0,7,0],
                 [6,0,0,0,5,0,0,0,8],
                 [0,0,0,6,0,3,9,0,5],
                 [0,1,8,0,0,5,0,0,0],
                 [0,0,6,8,3,2,7,0,1],
                 [7,5,3,1,9,0,4,8,0]]

grid = pandas.DataFrame(grid_original)

def block(number):
    number = int(number / 3) * 3
    return(number)

def check_possible(column, row, number):
        for check_number in range(9):
                #check if number already exits somewhere in column
                if number == grid[column][check_number]:
                        return False
                #check if number already exits somewhere in row
                elif number == grid[check_number][row]:
                        return False
        #transfer from column and row location to corresponding 3x3 block and check if number exits somewhere in block
        block_list = grid.iloc[block(row):block(row) + 3, block(column):block(column) + 3].values.tolist()
        for block_column in block_list:
            for block_element in block_column:
                if number == block_element:
                    return False
        return True

def check_finished():
    for row in grid.values.tolist():
        for element in row:
            if element == 0:
                return False
    print(grid)
    print("Finished!")
    #no return from nested function; just a dirty stop execution
    exit()

def solve():
        for column in range(9):
                for row in range(9):
                        if(grid[column][row] == 0):
                                for number in range(1,10): #10 not included
                                        if(check_possible(column, row, number)):
                                                grid[column][row] = number
                                                check_finished()
                                                solve()
                                        grid[column][row] = 0
                                return

#execute solving function
solve()
