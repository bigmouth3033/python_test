if __name__ == "__main__":
    name = input("Whom should I sign this to: ")

    with open("./txt/inscribed.txt", "w") as new_file:
        new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

    print("--------")
