def test_list():
    list = [1, 2, 3, 4, 5, 6]

    while True:
        index = int(input("index position: "))

        if index == -1:
            break

        value = int(input("what is the value"))

        list.insert(index, value)

    print(list)


def ask_remove_or_addition_in_list():
    list = []

    while True:
        user_input = input("a(d)d, (r)emove or e(x)it: ")

        if user_input == "d":
            if len(list) == 0:
                list.append(1)
                continue

            list.append(list[len(list) - 1] + 1)

        if user_input == "r":
            if len(list) == 0:
                print("nothing to remove!!!")
                continue

            list.pop(len(list) - 1)

        if user_input == "x":
            break

    print(list)


def ask_for_words():
    my_list = []

    while True:
        new_word = input("what is your word")

        count = 0
        while count < len(my_list):
            if my_list[count] == new_word:
                print(f"You typed in {len(my_list)} different words")
                return
            count = count + 1

        my_list.append(new_word)


def list_twice():
    list = []

    while True:
        number = int(input("New Item: "))

        if number == 0:
            return

        list.append(number)

        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")

def my_test(my_value : int):
    print(my_value)

my_test()