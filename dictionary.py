# create a dictionary
staffs = {
    'CEO': 'Junaid Bashir',
    'CTO': 'Michael Ross',
    'Sec': 'Daniel Hank',
    'CSO': 'Andre Putin'
}
# print with given key
print(staffs['CEO'])
# length of dictionary
print(len(staffs))
# see whether a KEY exists
print('CEO' in staffs)
# using get() to get dict data, second parameter is what should be displayed if it's not found
print(staffs.get('CTS', 'Position not found'))
# change key value
staffs['Sec'] = "Donna"
print(staffs['Sec'])
# update() adds a new key-value if the key parameter doesnt exist already, if it does, it replaces it
# update with existing key to repair:
staffs.update({'CSO':'Jack Griffin'})
print(staffs)
# update with a new key
staffs.update({'HOD': 'Bright Henderson'})
print(staffs)
# looping through the dictionary
for staff in staffs:
    print(staff)
    # this only prints the keys
# to print only values
for staff in staffs:
    print(staffs[staff])
# can also be done this way:
for staff in staffs.values():
    print(staff)
# to print key-value pairs
# loop through the .items to get the key & the value
for key, value in staffs.items():
    print(key, ":", value)
# copying a dictioinary
c_staffs = staffs.copy()
print(c_staffs)
print(staffs)
# deleting items
# NOTE: if you dont specify a key to delete, the whole dictionary will be deleted, including the name
del c_staffs["Sec"]
print(c_staffs)
# to remove all the key-values without deleting the dictionary, ise clear()
c_staffs.clear()
print (c_staffs)
# you can use pop to remove and item and even assigned the popped item to a variable
hod = staffs.pop("HOD")
print(staffs)
# display the popped value
print(hod)
# popitem removes the last key-value pair and you can store it as a tuple
cso = staffs.popitem()
print(cso)