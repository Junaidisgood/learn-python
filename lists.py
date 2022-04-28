# days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
# print(days[1])
# has_mon = "monday" in days
# if "moeday" in days:
#     print("Monday is part of list")
#     pass
# else:
#     print("Moeday is not in list")

#Create a list of strings.
letters = ["A", "B", "C", "D", "C", "E", "C"]
print("-------------------Default list-------------------")
print(letters)
print("-------------------Removing Cs-------------------")
while "C" in letters:
    letters.remove("C")
    pass
print(letters)
print("-------------------Cs Removed-------------------")
print("-------------------Removing first letter-------------------")
# pop value and stre to a variable
first = letters.pop(0)
print(letters)
print(first)
print("-------------------1st letter Removed-------------------")
print("-------------------Removing last letter-------------------")
letters.pop()
print(letters)
print("-------------------last letter Removed-------------------")
# delete letter with specified index
del letters[1]
print(letters)
# deletes all values
letters.clear()
print(letters)
# itearate through 1-100 and add only multiples of 10
for x in range(1, 100):
    if x%10 == 0:
        letters.append(x)
        pass

print(letters)

# count how many times a value appeared
val = 30
print(letters.count(val))

# find the index of a value
print(letters.index(val))

# string list
names = ["Junaid", "Bashir", "Mijinyawa", "Bello"]
# sort list alphabetically
names.sort()
print(names)
# copy list
names_rev = names.copy()
# reverse list
names_rev.reverse()
print(names_rev)