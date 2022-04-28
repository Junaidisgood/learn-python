word = "snorkel"
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "", "saturday", "sunday"]
for day in days:
    if day == "":
        print("Null")
        continue
    print(day)
print("done")