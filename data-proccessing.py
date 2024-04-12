
import urllib.request




if __name__ == "__main__":
    my_request = urllib.request.urlopen("https://helsinki.fi")
    print(my_request.read())
    print("____")