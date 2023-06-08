student_infos=[]
def print_menu():
    print("学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示所有学生信息")
    print("5.保存数据")
    print("0.退出系统")
def add_info():
    new_name = input("请输入新学生的姓名：")
    new_sex = input("请输入新学生性别：")
    new_phone = input("请输入新学生手机号：")
    new_infos={}
    new_infos['name']=new_name
    new_infos['sex']=new_sex
    new_infos['phone']=new_phone
    student_infos.append(new_infos)
def del_info(student):
    del_number = int(input("请输入要删除的序号："))-1
    del student[del_number]
def modify_info():
    student_id = int(input("请输入要修改的学生序号："))
    new_name = input("请输入新学生名字：")
    new_sex = input("请输入新学生性别：")
    new_phone= input("请输入新学生手机号：")
    student_infos[student_id - 1]['name']=new_name
    student_infos[student_id - 1]['sex']=new_sex
    student_infos[student_id - 1]['phone']=new_phone
def show_infos():
    print("学生信息如下：")
    print("序号 姓名 性别 手机号码")
    i=1
    for temp in student_infos:
        print("%d    %s     %s    %s     "%(i,temp['name'],temp['sex'],temp['phone']))
        i +=1
def save_to_file():
    file = open("backup.txt","w")
    file.write(str(student_infos))
    file.close()
def recover_data():
    global student_infos
    file=open("backup.txt")
    content=file.read()
    if content !="":
        student_infos = eval(content)
    file.close()
def main():
    recover_data()
while True:
    print_menu()
    key=input("请输入功能对应的数字：")
    if key=='1':
        add_info()
    elif key=='2':
        del_info(student_infos)
    elif key=='3':
        modify_info()
    elif key=='4':
        show_infos()
    elif key=='5':
        save_to_file()
    elif key=='0':
        quit_confirm = input("真的要退出吗？")
        if quit_confirm=="Yes":
            break
    else:
        print("输入有误，请重新输入")
main()