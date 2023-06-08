# with open('grade.txt', 'r') as f1, open('gradecopy.txt', 'w') as f2:
#     for line in f1:
#         if 'result' in line:
#             if '未通过' in line:
#                 continue
#         f2.write(line)

# # 打开原始文件和目标文件
# with open('grade.txt', 'r') as f1, open('gradecopy.txt', 'w') as f2:
#         # 逐行读取原始文件内容并写入目标文件
#     for line in f1:
#             # 判断当前行是否包含字符串 "result=未通过"
#         if 'result=未通过' not in line:
#                 # 如果不包含，则将该行数据写入目标文件中
#             f2.write(line)

# import shutil,os
# print(os.listdir())
# file = shutil.copy('grade.txt','gradecopy.txt')
# data = file.readlines()
# output = []
# for line in data:
#     if "未通过" not in line:
#         output.append(line)
# file.close()

# with open('grade.txt', 'r') as f:
#     lines = f.readlines()

# with open('gradecopy.txt', 'w') as f:
#     for line in lines:
#         if 'result' in line:
#             if '未通过' in line:
#                 continue
#         f.write(line)

# # 打开文件
# with open("grade.txt", "r") as file:
#     # 读取文件内容
#     lines = file.readlines()

# # 过滤出"通过"的学生信息
# passed_students = [line for line in lines if line.split(",")[-1].strip() == "通过"]

# # 将过滤结果写回文件
# with open("gradecopy.txt", "w") as file:
#     file.writelines(passed_students)

# 打开原始文件和目标文件
with open('grade.txt', 'r', encoding='utf-8') as f, open('gradecopy.txt', 'w') as fw:
    # 遍历每行数据
    for line in f:
        # 如果“result”一栏不为“未通过”，则写入到目标文件中
        if not line.strip().endswith("未通过"):
            fw.write(line)