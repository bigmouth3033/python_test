def double_items(numbers: list) -> list:
    new_list = numbers[:]

    for i in range(len(new_list)):
        new_list[i] = new_list[i] * 2

    return new_list


def remove_smallest(numbers: list) -> None:
    smallest_item = numbers[0]

    for number in numbers:
        if number < smallest_item :
            smallest_item = number

    new_list = []

    for number in numbers :
        if number != smallest_item :
            new_list.append(number)
    
    numbers[:] = new_list

def print_sudoku(sudoku: list) -> None :
    for i in range(len(sudoku)):
        string = ""

        for j in range(len(sudoku[i])):
            if sudoku[i][j] != 0:
                string += str(sudoku[i][j])
            else :
                string += "-"
            string += "  "
        
        print(string)


def add_number(sudoku: list, row_no: int, column_no: int, number:int) :
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) :
    new_sudoku = []

    for row in sudoku:
        new_sudoku.append(row[:])
        
    new_sudoku[row_no][column_no] = number
    
    return new_sudoku





def main() -> None:
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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
    return None


if __name__ == "__main__":
    main()
