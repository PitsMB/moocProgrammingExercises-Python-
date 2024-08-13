# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:

# Write your solution here
def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = [row.copy() for row in sudoku]
    new_list[row_no][column_no] = number
    return new_list

    

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print(sudoku)
    print(grid_copy)
    # print("Original:")
    # print_sudoku(sudoku)
    # print()
    # print()
    # print("Copy:")
    # print_sudoku(grid_copy)