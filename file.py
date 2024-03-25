def largest():
    largest_number = None

    with open("numbers.txt") as new_file:
        for number in new_file:
            if largest_number == None:
                largest_number = int(number)

            if int(number) > largest_number:
                largest_number = int(number)

    print(largest_number)


def word_with_csv():
    with open("grades.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            list_line = line.split(";")
            name = list_line[0]
            grade = list_line[1:]
            print(name)
            print("\t" + str(grade))


def read_fruits():
    fruit_dictionary = {}

    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            list_line = line.split(";")
            fruit_dictionary[list_line[0]] = list_line[1]

    return fruit_dictionary


def matrix_sum(name_file: str) -> int:
    sum = 0
    with open(name_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            list_number = line.split(",")

            for number in list_number:
                sum += int(number)

    return sum


def matrix_max(name_file: str) -> int:
    max = None

    with open(name_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            list_number = line.split(",")

            for number in list_number:
                if max == None:
                    max = int(number)

                if int(number) > max:
                    max = int(number)

    return max


def row_sums(name_file: str) -> list:
    list_row = []

    with open(name_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            list_number = line.split(",")
            sum = 0
            for number in list_number:
                sum += int(number)

            list_row.append(sum)

    return list_row


def get_file_content(file_name: str) -> list:
    list_content = []

    with open(file_name) as new_file:
        for line in new_file:
            list_content.append(line)

    return list_content


def grades_processing():
    grades = {}

    with open("grades.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            list_line = line.split(";")
            grades[list_line[0]] = []

            for grade in list_line[1:]:
                grades[list_line[0]].append(int(grade))

    for name, grades in grades.items():
        best_grade = max(grades)
        average = sum(grades) / len(grades)
        print(f"name: {name}, best grade is {best_grade:.2f}, average is {average:.2f}")


def student_processing():
    if False:
        student_file_name = input("Student information: ")
        student_file_grade = input("Exercises completed:")
    else:
        student_file_name = "./csv/student.csv"
        student_file_grade = "./csv/student_grades.csv"

    names = {}

    with open(student_file_name) as new_file:
        for line in new_file:
            list_line = line.split(";")

            if list_line[0] == "id":
                continue

            names[list_line[0].strip()] = list_line[1].strip() + " " + list_line[2].strip()

    grades = {}

    with open(student_file_grade) as new_file:
        for line in new_file:
            list_line = line.split(";")

            if list_line[0] == "id":
                continue

            grades[list_line[0]] = []

            for grade in list_line[1:]:
                grades[list_line[0]].append(int(grade))

    for id, name in names.items():
        if id in grades:
            total_grade = sum(grades[id])
            print(f"{name} {total_grade}")


if __name__ == "__main__":
    student_processing()

    print("-------")
