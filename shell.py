import QJL


def from_console():
    while True:
        text = input("QJL >")
        # termination
        if text == "886":
            return 
        if text.strip() == "": continue
        #run the compiler and interpreter
        result, error = QJL.run('<Console input from user>',text)
        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))

def from_file(filename):
    f = open(filename, 'r')
    content = f.read()
    print(content)
    result, error = QJL.run('test',content)
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))


from_console()
# from_file("test.txt")
# from_file("break.txt")