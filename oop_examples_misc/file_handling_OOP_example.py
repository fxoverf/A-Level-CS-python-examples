def writeFile_Line(write):
    try:
        with open("data.txt", "w") as file:
            file.write(write)
            print("File written")
    except OSError as err:
        print("write error:", err)
def readFile_Line():
    try:
        with open("data.txt", "r") as file:
            line = file.read()
            print("read from file: \n", line)
    except FileNotFoundError:
        print("File not found")
    except OSError as err:
        print("File read error", err)
def appendFile_Line(append):
    try:
        with open("data.txt", "a") as file:
            file.write(f"\n {append}")
    except OSError as err:
        print("append error:", err)

#main program

writeFile_Line("hello")
readFile_Line()
appendFile_Line("world")
readFile_Line()

