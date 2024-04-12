from datetime import datetime




if __name__ == "__main__":
    try:
        datetime(year=2024, month=11, day=31)
    except ValueError:
        print("value of date out of range")
