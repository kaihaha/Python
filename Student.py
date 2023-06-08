class Student:
    def __init__(self, id, name, age, gender, score):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"学生 {student.name} 添加成功！")

    def search_student(self):
        if not self.students:
            print("当前没有任何学生信息！")
            return
        for student in self.students:
            print(f"学号：{student.id}\n姓名：{student.name}\n年龄：{student.age}\n性别：{student.gender}\n成绩：{student.score}")

    def modify_student(self, id, student):
        for i, s in enumerate(self.students):
            if s.id == id:
                self.students[i] = student
                print(f"学生 {student.name} 修改成功！")
                return
        print("未找到该学生！")

    def delete_student(self, id):
        for i, student in enumerate(self.students):
            if student.id == id:
                del self.students[i]
                print("删除成功！")
                return
        print("未找到该学生！")

if __name__ == "__main__":
    sm = StudentManagement()

    while True:
        print("\n1. 添加学生\n2. 查看学生信息\n3. 修改学生信息\n4. 删除学生\n5. 退出程序")
        choice = input("请输入操作选项：")

        if choice == "1":
            id = input("请输入学号：")
            name = input("请输入姓名：")
            age = input("请输入年龄：")
            gender = input("请输入性别：")
            score = input("请输入成绩：")

            student = Student(id, name, age, gender, score)
            sm.add_student(student)

        elif choice == "2":
            sm.search_student()

        elif choice == "3":
            id = input("请输入要修改的学生学号：")
            new_id = input("请输入新学号：")
            new_name = input("请输入新姓名：")
            new_age = input("请输入新年龄：")
            new_gender = input("请输入新性别：")
            new_score = input("请输入新成绩：")

            new_student = Student(new_id, new_name, new_age, new_gender, new_score)
            sm.modify_student(id, new_student)

        elif choice == "4":
            id = input("请输入要删除的学生学号：")
            sm.delete_student(id)

        elif choice == "5":
            break

        else:
            print("输入有误，请重新输入！")