#list
student = ["Rahul", "Amit", "Sneha", "Priya"]

print("Student List:", student)
print("First Student:", student[0])

student.append("Rohit")
student.remove("Amit")

print("Updated List:", student)


#Tuple 

marks = (85, 90, 78, 92, 88)
print("Marks:", marks)
print("First Mark:", marks[0])
print("Total Marks:", sum(marks))
print("Number of Subjects:", len(marks))

# Set (set)

numbers = {10, 20, 30, 20, 40, 10}
print("Set:", numbers)
numbers.add(50)
numbers.remove(30)
print("Updated Set:", numbers)

#Dictionary

# Program to demonstrate Dictionary

student = {
    "Name": "Rahul",
    "Roll_No": 101,
    "Course": "BCA",
    "Marks": 85
}

print("Student Details:")
print("Name:", student["Name"])
print("Roll No:", student["Roll_No"])
print("Course:", student["Course"])
print("Marks:", student["Marks"])

# Add a new key-value pair
student["Grade"] = "A"

print("Updated Dictionary:", student)