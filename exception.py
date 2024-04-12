def read_input(input_str: str, start: int, end: int) -> int:
    while True:
        try:
            input_value = int(input(input_str))

            if input_value >= start and input_value <= end:
                return input_value
        except ValueError:
            print("wrong data type")


def new_person(name: str, age: int) -> tuple:
    if not isinstance(name, str):
        raise TypeError("That is not a fucking string you idiot!")

    if not isinstance(age, int):
        raise TypeError("That is not a fucking number you piece of shit!")

    if age <= 0:
        raise ValueError("Age must be greater than 0!")

    return name, age


def check_duplicate(list_number: list):
    sorted_list = sorted(list_number)

    for i in range(len(sorted_list)):
        if i == 0:
            continue

        if int(sorted_list[i]) == int(sorted_list[i - 1]):
            return False

    return True


def filter_incorrec():
    file_name = "correct_numbers.csv"
    correct = {}

    with open("./csv/lottery.csv") as my_file:
        for line in my_file:
            split_line = line.split(";")
            week = split_line[0]
            split_number = split_line[1].split(",")

            if len(split_number) < 7:
                continue

            try :
                if not check_duplicate(split_number):
                    continue
            except: 
                continue

            for number in split_number:
                if int(number)  < 1 or int(number) >39:
                    continue
            
            try :
                converted_week = int(week[5:])
            except :
                continue
            
            correct[week] = split_number

    with open(file_name, "w") as my_file:
        for key, value in correct.items():
            my_file.write(f"{key};{",".join(value)}")




if __name__ == "__main__":
    filter_incorrec()


    print("-----------")
