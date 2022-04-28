import csv
with open('children.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if (row[1] == 'OLIVIA' or row[2] == 'OLIVIA'):
            # check parent first that has a paremt(grandparentto child) OLIVIA
            x =row[0]
            for row1 in reader:
                # check if the child has a parent name as the parent name gotten above
                if(row1[1] == x or row1[2] == x):
                    print(row1)

    pass