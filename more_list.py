def longest(strings: list) -> str:
    longest_string = strings[0]

    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string


def count_matching_elements(my_matrix: list, element: int) -> int: 
    count = 0
    
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if(my_matrix[i][j] == element):
                count += 1
                

    return count


def main() -> None:
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
    return


if __name__ == "__main__":
    main()
