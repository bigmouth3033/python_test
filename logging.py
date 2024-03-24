def add_with_logging(first_string: str, second_string: str):
    result = ""
    length = len(first_string) if len(first_string) >= len(second_string) else len(second_string)
    residual = 0

    print(f"Ta có {first_string} cộng với {second_string}")

    first_string = first_string[::-1]
    second_string = second_string[::-1]

    for i in range(length):
        first_value = first_string[i] if i < len(first_string) else 0
        second_value = second_string[i] if i < len(second_string) else 0
        print(f"Bước thứ {i + 1} ta lay {first_value} cộng với {second_value} cộng với số dư là {residual}")

        total = int(first_value) +  int(second_value) + residual
        print(f"Ta có tổng là {total}")

        residual = total // 10 if total >= 10 else 0
        new_value  = total - (residual * 10) 

        print(f"Ta lấy {new_value} thêm vào")

        if residual != 0:
            print(f"Và nhớ {residual}")

        result += str(new_value)
        print(f"Ta được {result[::-1]}")
    
    if residual != 0 :
        result += str(residual)
        print(f"Và bước cuối cùng ta thêm vào số dư {residual}")

    return result[::-1]



def unit_test_for_add():
    test_value = {
        1 : ["2342", '545465'],
        2 : ['9999991' , '435345345'],
        3 : ['34534532421', '2323'],
        4 : ['5398','4534634634'],
        5 : ['214542', '4423'],
        6 : ['99','99999'],
        7 : ['121', '435435'],
        8 : ['12', '2353463'],
        9 : ['23', '46464646']
    }

    for index in test_value:
        if int(add_with_logging(test_value[index][0], test_value[index][1])) != (int(test_value[index][0]) + int(test_value[index][1])):
            return False 

    return True






def main() -> None:
    print(unit_test_for_add());
    return None


if __name__ == "__main__":
    main()
