menu = {'Wonton Soup' : 2.25, 'Egg Drop Soup' : 2.00, 'Hot & Sour Soup' : 2.75,
	'Egg Roll' : 1.75, 'Dumplings' : 8.00, 'Spare Ribs' : 8.00,
	"General Tso's Chicken" : 16.00, 'Moo Shu Pork' : 15.00, 
	'Chicken with Garlic Sauce' : 15.00, 'Chow Fun' : 13.00 }
lisaAndJeffsOrder = ['Hot & Sour Soup', 'Dumplings', 'Chicken with Garlic Sauce']
jillAndJacksOrder = ['Wonton Soup', 'Spare Ribs', "General Tso's Chicken"]
for i in lisaAndJeffsOrder:
    output=f"""
    {i}: {menu[i]:>10,.2f}
    """
    total = menu[i]
    total = total + menu[i]
    print(output)
print("---------------------------------------------")
output_t=f"""
    Total: {total:>30,.2f}
"""
print(output_t)