names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
# sort won't work because it sees lower cases as higher ASCII codes
# try using a sort filter, len won't work in our case
names.sort(key=len)
print(names)