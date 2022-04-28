name = "Junaid"
print(f"Hello {name}")
price = 49.99
qty = 30
# use comma to place commas in thousand place and .2f for 2d.p
print(f"Subtotal: ${qty*price: ,.2f}")
# PERCENT NUMBERS
tax = 0.075
# .2% will print percentage with 2dp
print(f"Sales tax rate: {tax: .2%}")
# multi-line format
user1 = "mahmud"
user2 = "Junaid"
user3 = "usman"
# 2 different methods to break lines
print(f"{user1} \n{user2} \n{user3}")
print(f"""
user1
user2
user3
""")
# alignment(<-left, ^-center, >-right) with a preceding number of letters(width)
subtotal = qty * price
taxx = tax * subtotal
total = subtotal + taxx 
output=f"""
Subtotal : ${subtotal:>9,.2f}
Sales Tax: ${taxx:>9,.2f}
Total    : ${total:>9,.2f}
"""
print(output)
# attach the dollar sign to the value not like above
# first reformat the values and assign to new variables
s_subtotal = "$" + f"{subtotal:,.2f}"
s_taxx = "$" + f"{taxx:,.2f}"
s_total = "$" + f"{total:,.2f}"
# output the values with dollar sign attached
output=f"""
Subtotal : {s_subtotal:>9}
Sales Tax: {s_taxx:>9}
Total    : {s_total:>9}
"""
print(output)