def read_file(file_name):
    try:
        with open(file_name) as new:
            text = new.read()
            new.close()
            print(text)
    except FileNotFoundError:
        print("<<< FILE NOT FOUND >>>")


def write_file(file_name, plus_text):
    try:
        with open(file_name, 'a') as open_file:
            open_file.write(plus_text)
            open_file.close()
    except FileNotFoundError:
        print("<<< FILE NOT FOUND >>>")


read_file("file.txt")
write_file("file.txt", " Oleg")
read_file("file.txt")
