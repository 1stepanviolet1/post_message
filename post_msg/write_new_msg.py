import os

filename = os.path.join('.', 'messages.html')


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

    try:
        write_msg(data)
    except KeyError:
        exit(321)
    else:
        exit(0)

if __name__ == "__main__":
    main()
    try:
        print()
    except PermissionError:
        exit(111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
    except BaseException:
        exit(123)

