dictionary = {'Alice':85,'Sree':99,'Naidu':79}
student_name = input("Enter the student's name: ")
if student_name in dictionary:
    print(f"{student_name}'s marks: {dictionary[student_name]}")
else:
    print("Student not found.")