import os


def write_diary():
    file_name = "./txt/diary.txt"

    op = None

    while op != 0:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        op = int(input("Function: "))

        if op == 1:
            with open(file_name, "a") as new_file:
                new_line = input("Diary entry: ")
                new_file.write(f"{new_line}\n")

        if op == 2:
            with open(file_name) as new_file:
                for line in new_file:
                    line = line.strip()
                    print(line)

    print("Bye Now")


def cal(first_value: int, second_value: int, operator: str) -> int:
    if operator == "+":
        return first_value + second_value

    if operator == "-":
        return first_value - second_value

    if operator == "*":
        return first_value * second_value

    if operator == "/":
        return first_value / second_value


def filter_solution():
    file_name = "./csv/solutions.csv"

    right_solution = []
    wrong_solution = []

    with open(file_name) as my_file:
        for line in my_file:
            line_item = line.split(";")

            name = line_item[0].strip()
            expression = line_item[1].strip()
            result = line_item[2].strip()

            if cal(int(expression[0]), int(expression[2]), expression[1]) == int(
                result
            ):
                right_solution.append(f"{name};{expression};{result}\n")
            else:
                wrong_solution.append(f"{name};{expression};{result}\n")

    with open("./csv/correct.csv", "w") as my_file:
        for item in right_solution:
            my_file.write(item)

    with open("./csv/incorrect.csv", "w") as my_file:
        for item in wrong_solution:
            my_file.write(item)


def store_personal_data(person: tuple):
    name_file = "./csv/people.csv"

    (name, age, height) = person

    with open(name_file, "a") as my_file:
        my_file.write(f"{name};{age};{height}\n")


if __name__ == "__main__":
    store_personal_data(("Ngo Dinh Tan", 27, 178.9))

    print("--------")
