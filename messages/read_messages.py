import os


filename = os.path.join('/', 'var', 'www', 'messages.html')


def read_file() -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return lines


def main():
    try:
        lines = read_file()
    except FileNotFoundError:
        print("ERROR: FileNotFound")
        print("Check your path to messages.html")

    print(*lines, sep='\n')


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print("Ouups..")
        print("Sorry, I don't know this error..")

