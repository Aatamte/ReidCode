from utils.test_functions import complete


def print_hi():
    return "Hello"


if __name__ == '__main__':
    var = print_hi()
    print(var)
    assert print_hi() == "Hello"



