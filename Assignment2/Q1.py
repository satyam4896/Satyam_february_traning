class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def display_details(self):
        print(self.__user_id, self.__name)


class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__courses = []

    def enroll_course(self, course):
        self.__courses.append(course)

    def get_courses(self):
        return self.__courses

    def display_details(self):
        print("Student ID:", self.get_id())
        print("Name:", self.get_name())
        print("Courses:", self.__courses)


class Mentor(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__students = []

    def assign_student(self, student):
        self.__students.append(student)

    def view_students(self):
        for s in self.__students:
            print(s.get_name())

    def display_details(self):
        print("Mentor ID:", self.get_id())
        print("Name:", self.get_name())
        print("Assigned Students:", [s.get_name() for s in self.__students])


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def view_all(self, students, mentors):
        print("\nAll Students:")
        for s in students:
            s.display_details()
        print("\nAll Mentors:")
        for m in mentors:
            m.display_details()

    def display_details(self):
        print("Admin ID:", self.get_id())
        print("Name:", self.get_name())


students = []
mentors = []

admin = Admin("A1", "Admin")

while True:
    print("\n1. Add Student")
    print("2. Add Mentor")
    print("3. Enroll Course")
    print("4. Assign Student to Mentor")
    print("5. Mentor View Students")
    print("6. Admin View All")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        students.append(Student(sid, name))

    elif choice == "2":
        mid = input("Enter Mentor ID: ")
        name = input("Enter Name: ")
        mentors.append(Mentor(mid, name))

    elif choice == "3":
        sid = input("Enter Student ID: ")
        course = input("Enter Course: ")
        for s in students:
            if s.get_id() == sid:
                s.enroll_course(course)

    elif choice == "4":
        sid = input("Enter Student ID: ")
        mid = input("Enter Mentor ID: ")
        student_obj = None
        for s in students:
            if s.get_id() == sid:
                student_obj = s
        for m in mentors:
            if m.get_id() == mid and student_obj:
                m.assign_student(student_obj)

    elif choice == "5":
        mid = input("Enter Mentor ID: ")
        for m in mentors:
            if m.get_id() == mid:
                m.view_students()

    elif choice == "6":
        admin.view_all(students, mentors)

    elif choice == "7":
        break