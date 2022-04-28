# accept all names and print in a given format
# first = input("Enter First Name: ")
# mid = input("Enter Middle Name: ")
# last = input("Enter Last Name: ")
# middle = str(mid)
# print("Fullname: " + first + " " + middle[0].upper() + ". " + last)

s = "Whatever You Do Be The Best At It, Whatever You Become, Be The Best"
# is there a lowercase t in string "s"?
print("t" in s)
# is there an uppercase t in string "s"?
print("T" in s)
# print 15 hypens(-)
print("-" * 15)
# print first character in string s
print(s[0])
# print characters 33-39 in string s
print(s[33:39])
# print every 3rd character in s starting from 0
print(s[0:44:3])
# print lowest character in s (space<a<b<c...<z)
print(min(s))
# print lowest character in s (z>y>x...>a>space)
print(max(s))
# where is the first uppercase B - returns error if none is found
print(s.index("B"))
# where is the first lowercase O between char 12 & 44
# note that the returned value still starts counting from zero
print(s.index("o", 12, 44))
# how many lowercase letters a are in string s?
print(s.count("a"))