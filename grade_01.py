with open('grade.txt', 'r',encoding='utf-8') as f, open('gradecopy.txt', 'w') as fw:
    for line in f:
        if not line.strip().endswith("未通过"):
            fw.write(line)

# with open('grade.txt', 'r',encoding='utf-8') as file:
#     lines = file.readlines()

# passed_students = [line for line in lines if line.split(",")[-1].strip() == "通过"]

# with open('gradecopy.txt', 'w') as file:
#     file.writelines(passed_students)


# # 打开grade.txt文件
# file = open("grade.txt", "r",encoding='utf-8')

# # 读取文件内容
# data = file.readlines()

# # 创建一个空列表用于存储有效行
# output = []

# # 处理文件内容
# for line in data:
#     if "未通过" not in line:
#         # 将有效行添加到输出列表中
#         output.append(line)

# # 关闭输入文件
# file.close()

# # 创建输出文件
# output_file = open("gradecopy.txt", "w")

# # 将结果写入输出文件
# for line in output:
#     output_file.write(line)

# # 关闭输出文件
# output_file.close()