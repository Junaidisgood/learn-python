# create a set "sample_set"
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)
# adds a value to set
sample_set.add(11.23)
print(sample_set)
# update() to add multiple items to a set - items are added in form of a list [square brackets]
sample_set.update([88, 123.45, 2.98])
print(sample_set)
# set can be duplicated but the order maybe different as items are not indexed
sample2 = sample_set.copy()
print(sample2)

# Note: you cannot change the order of items as they are not indexed - functions like sort(), reverse() wont work