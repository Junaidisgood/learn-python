def main():
    f = open('lines.txt', 'r') 
    # param 1 - file name, param 2:
    # r - read only
    # w - write only(empties file)
    # a - appends the data in files - continue editing
    # rw - optional, to read and write
    # use '+' to use multiple options, e.g r+w
    for line in f:
        print(line.lstrip())

main()