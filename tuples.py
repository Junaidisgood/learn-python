# create a tuple - prices
prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(prices)
# print length of tuple
# had to convert to string to be able to print, function is len(object)
print("Length of tuple: " + str(len(prices)))
# count() shows how many times a value occured in the tuple
print("4.95 occured " + str(prices.count(4.95)) + " time(s)")
# returns true if value exists :
if(4.95 in prices):
    print("4.95 exists in the tuple")
else:
    print("4.95 doesnt exist in the tuple prices")

# check the index of price, to avoid error, you check if it exists first
look = 12345
if look in prices:
    position = prices.index(look)
else:
    position = -1
print(position)

# loop through and display all the tuples
for price in prices:
    print(f"${price: .2f}")

# Note: you cant change the values of a tuple
# as in below
# prices[1] = 123.45