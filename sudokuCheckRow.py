# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# Write your solution here
def row_correct(sudoku: list, row_no):
    my_row = sudoku[row_no]
    new_list = []

    for i in my_row:
        if i in new_list and i != 0:
            return False
        else:
            new_list.append(i)
    return True




if __name__ == "__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))