def hello(): #example function
    """A docstring describing the function"""
    print("Hello")

hello()

def hello_x(x): #passing parameters
    print("Hello "+x)

name = "Junaid"
hello_x(name) #passing name as x

def optional_param(user = "null"): #optional parameters functions
    print("Hello "+user)
# if parameter is not passed, it ses the already defined parameter in the function definition
optional_param()

def multiple_param(fname, lname, datestring): #passing multiple parameters
    print("Hello "+fname+" "+lname)
    print("The date is "+datestring)
multiple_param("Junaid", "Bashir", "12/01/1991")

def optional_multiple(fname, lname, datestring=''): #passing multiple parameters with optional parameter
    """The optional parameter should come last"""
    msg = "Hello "+fname+" "+lname
    if len(datestring)>0:
        msg+=" you mentioned "+ datestring
        print(msg)
optional_multiple("Junaid", "Bashir", "18/01/2001")

def unarranged_params(fname, lname):#passing the functions in a reverse order
    print("Hello "+fname+" "+lname)
unarranged_params(lname="Bashir", fname="Junaid")

def alphabetize(list=[]):
    """Pass any list in square brackets, displays a string with items sorted"""
    # make a copy of the passed string
    sorted_list = list.copy()
    # sort the copied list
    sorted_list.sort()
    # create empty string for output
    final_list = ""
    # loop through list and appen name and comma and space
    for x in sorted_list:
        final_list += x + ", "
    # Knock of last comma space if final list is long enough
    final_list = final_list[:-2]
    # print the sorted list stored in string
    print(final_list)
alphabetize(['Junaid', 'Bashir', 'Bello', 'Mijinyawa'])

def sorter(*args): #pass any amount of parameters directly
    """Pass in any anumber of arguments seperated by commas
    Inside the function, they are treated as a tuple named args"""
    #The passed-in
    # Create a list from the passed-in tuple
    newlist = list(args)
    # sort and show the new list
    newlist.sort()
    print(newlist)
sorter(1, 0.1, 0.01, 0.001, 10, 100)

def return_value(list=[]):
    """Function can be assigned to a variable to store the returned value"""
    # make a copy of the passed string
    sorted_list = list.copy()
    # sort the copied list
    sorted_list.sort()
    # create empty string for output
    final_list = ""
    # loop through list and appen name and comma and space
    for x in sorted_list:
        final_list += x + ", "
    # Knock of last comma space if final list is long enough
    final_list = final_list[:-2]
    # return the sorted list stored in string
    return(final_list)
# assing function return value to a var
new = return_value(['Junaid', 'Bashir', 'Bello', 'Mijinyawa'])
# print variable
print(new)