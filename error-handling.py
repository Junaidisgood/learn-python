def main():
    try:
        x = 5/2
    # specify type of error to except
    except ValueError:
        print("Cannot convert string to int")
    except ZeroDivisionError:
        print("Numbers cannot be divided by zero")
    # except any error/ no need to specify
    except:
        print("Unknown error")
    # if it works - enter the else block
    else:
        print(x)

main()