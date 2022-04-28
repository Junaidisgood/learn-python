print("Enter your grade: ")
grade = int(input())
if grade == 0:
    print("Kindergaten")
elif grade>0 and grade<=8:
    print("Elementary school")
elif grade>8 and grade<=12:
    print("High school")
elif grade>12 and grade<16:
    print("College")
else:
    print("Invalid input")