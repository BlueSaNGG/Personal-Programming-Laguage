from logging import basicConfig
import QJL


def from_console():
    while True:
        text = input("QJL >")
        result, error = QJL.run('<Console input from user>',text)
        if error:
            print(error.as_string())
        else:
            print(result)
            

def from_file(filename):
    f = open('test.txt', 'r')
    content = f.read()
    # print(content)
    result, error = QJL.run('test',content)
    if error:
        print(error.as_string())
    else:
        print(result)


from_console()