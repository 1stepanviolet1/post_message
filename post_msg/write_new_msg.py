import os

filename = os.path.join('/', 'var', 'www', 'post_msg', 'messages.html')


def write_msg(data: dict) -> None:
    lines = []

    lines.append("<p>\n")

    lines.append(f"<b>Name:</b> {data['name']} <br>\n")

    lines.append(f"<b>Email:</b> {data['email']} <br>\n")

    lines.append("<br>\n")

    lines.append(f"<em>Message:</em> <br>\n")
    lines.append(f"{data['msg']} <br>\n")

    lines.append("</p>\n")
    lines.append("<hr>\n\n")

    with open(filename, 'a', encoding='utf-8') as file:
        file.writelines(lines)


def main():
    data = (el.split(':') for el in input().split(';', 2))
    data = {key: val for key, val in data}

    write_msg(data)
    

if __name__ == "__main__":
    try:
        main()
    except KeyError:
        print("Oups..")
        print("Invalid data")
    except PermissionError:
        print("Sorry :(")
        print("Permission denied..")
    except BaseException:
        print("Ouuu...")
        print("I don't know this error :(")
        print("Connect to developer")
    else:
        print("Success :)")
        print("You message posted!")

