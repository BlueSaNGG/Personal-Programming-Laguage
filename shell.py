import QJL


def from_console():
    while True:
        text = input("QJL >")
        # termination
        if text == "886":
            return 
        #run the compiler and interpreter
        result, error = QJL.run('<Console input from user>',text)
        if error:
            print(error.as_string())
        else:
            print(result)
            

def from_file(filename):
    f = open(filename, 'r')
    content = f.read()
    print(content)
    result, error = QJL.run('test',content)
    if error:
        print(error.as_string())
    else:
        print(result)


from_console()
# from_file("test.txt")