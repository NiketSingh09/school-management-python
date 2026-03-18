#school folder

class School:
    school_name = "XYZ SCHOOL"
    def __init__(self , name , address , age , father , mother):
        self.name = name
        self.address = address
        self.age = age
        self.father = father
        self.mother = mother
    def hello(self):
        print("Thank you so much for taking addmission in our school")

def add_student(name , address , age , father , mother):
    print("HEllo " , name , "you have successfully got addmissioned in our school")

# ----------------------------------------------------------------------------------------

while True:
    student_name = input("enter your name : ")
    student_address = input("enter your address : ")
    student_age = int(input("enter your age : "))
    student_father = input("enter your father's name : ")
    student_mother = input("enter your mother's name : ")

    print("Writing data...")  # DEBUG

    with open("student.txt", "a") as f:
        f.write(f"Name: {student_name}\n")
        f.write(f"Address: {student_address}\n")
        f.write(f"Age: {student_age}\n")
        f.write(f"Father: {student_father}\n")
        f.write(f"Mother: {student_mother}\n")
        f.write("----------------------\n")

    print("Done writing!")  # DEBUG

    choice = input("Add another? (y/n): ")
    if choice != "y":
        break