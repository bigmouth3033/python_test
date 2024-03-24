def times_ten(start_index: int, end_index: int):
    new_dictionary = {}
    for i in range(start_index, end_index + 1):
        new_dictionary[i] = i * 10

    return new_dictionary


def factorials(n: int):
    new_dictionary = {}

    for i in range(1, n + 1):
        if i == 1:
            new_dictionary[1] = 1
            continue

        new_dictionary[i] = i * new_dictionary[i - 1]

    return new_dictionary


def counts(my_list):
    dictionary = {}
    for item in my_list:
        if item in dictionary:
            dictionary[item] = dictionary[item] + 1
        else:
            dictionary[item] = 1

    return dictionary


def categorize_by_initial(my_list):
    group = {}

    for word in my_list:
        initial_letter = word[0]

        if initial_letter not in group:
            group[initial_letter] = []

        group[initial_letter].append(word)

    return group


def histogram(string: str) -> None:
    dictionary = {}

    for word in string:
        if word not in dictionary:
            dictionary[word] = 0

        dictionary[word] += 1

    for key, value in dictionary.items():
        print(f"{key} {"*" * value}")


def phone_book() -> None:
    books = {}

    while True:
        op = int(input("command (1 search, 2 add, 3 quit):"))

        if op == 2:
            name = input("name: ")

            if name not in books:
                books[name] = []
            
            books[name].append(input("number:"))

        if op == 1 :
            name = input("name: ")

            if name in books:
                for number in books[name]:
                    print(number)
            
            if name not in books:
                print("no number")

        if op == 3 :
            print("exit!")
            return



def invert(dictionary: dict) -> None:
    temp_dictionary = {}

    for key, value in dictionary.items():
        temp_dictionary[value] = key
    
    dictionary.clear()

    for key, value in temp_dictionary.items():
        dictionary[value] = key

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_movie = {
        "name" : name,
        "director" : director,
        "year" : year,
        "runtime" : runtime
    }

    database.append(new_movie)





def find_movies(database: list, search_term: str) -> list:
    search_movie = []

    for movie in database:
        if search_term.lower() in movie["name"].lower():
            search_movie.append(movie)

    return search_movie

def main() -> None:
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)
    return None

if __name__ == "__main__":
    main()
