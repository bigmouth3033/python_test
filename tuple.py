def create_tuple(x: int, y: int, z: int) -> tuple:
    my_list = sorted([x, y, z])
    return (my_list[0], my_list[2], my_list[0] + my_list[1] + my_list[2])


def oldest_person(people: list):
    index = 0

    for i in range(len(people)):
        if people[i][1] < people[index][1]:
            index = i

    return people[index][0]


def older_people(peoples: list, year: int):
    list_of_old = []

    for people in peoples:
        if people[1] <= year:
            list_of_old.append(people[0])

    return list_of_old


def add_student(student_group: list, name: str):
    if name not in student_group:
        student_group[name] = []


def print_student(student_group: list, name):
    if name not in student_group:
        print(f"{name} : no such person in the database")
        return

    if len(student_group[name]) == 0:
        print(name + ":")
        print("  no completed courses")
        return

    print(f"{name}: ")
    print(f"{len(student_group[name])} completed course")

    total = 0

    for student_name, point in student_group[name]:
        total = total + point
        print("\t" + student_name, point)

    print(f"\t average grade is {(total / len(student_group[name])):.2f}")


def add_course(student_group: list, name, course: tuple) -> None:
    if course[1] == 0:
        return

    if name not in student_group:
        print(f"{name} : no such person in the database")
        return

    temp_index = -1

    for i in range(len(student_group[name])):
        if student_group[name][i][0] == course[0]:

            if student_group[name][i][1] >= course[1]:
                return

            temp_index = i

    if temp_index != -1:
        student_group[name].pop(temp_index)

    student_group[name].append(course)


def summary(student_group: list) -> None:
    print(f"student {len(student_group)}")

    max_course_completed = 0
    max_course_name = None
    best_avarage = 0
    best_avarage_name = None

    for name, course in student_group.items():
        if len(course) > max_course_completed:
            max_course_completed = len(course)
            max_course_name = name

        total = 0
        for item in course:
            total += item[1]

        avarage = total / len(course)

        if avarage > best_avarage:
            best_avarage = avarage
            best_avarage_name = name

    print(f"most courses completed {max_course_completed} {max_course_name}")

    print(f"best average grade {best_avarage:.2f} {best_avarage_name}")


def square_of_letter(number: int) -> None:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    square = []
    square.append(["A"])

    for index in range(1, number):
        for item in square:
            item.insert(0, alphabet[index])
            item.append(alphabet[index])

        square.insert(0, list(alphabet[index] * len(square[0])))
        square.append(list(alphabet[index] * len(square[0])))

    return square


if __name__ == "__main__":
    my_tuple = 1, 2, 4

    new_tuple =  "a", my_tuple, "b"

    print(new_tuple)    
    print("-----")
