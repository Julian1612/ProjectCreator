import os
import shutil
import time

# def insert_makefile_content(project_info):
#     with open("./templets/makefile/Makefile", 'r') as file:
#         lines = file.readlines()

#     variables = ['NAME', 'SRC', 'HEADER']
#     updated_lines = []
#     for line in lines:
#         for variable in variables:
#             if line.startswith(variable):
#                 updated_line = line.strip()
#                 updated_line += ' ' + project_info.get(variable, '') + '\n'
#                 updated_lines.append(updated_line)
#                 break
#         else:
#             updated_lines.append(line)

#     output_file = os.path.join("./", os.path.basename("./Makefile"))
#     with open(output_file, 'w') as file:
#         file.writelines(updated_lines)


import os

def insert_makefile_content(project_info):
    makefile_path = './templets/makefile/Makefile'
    output_dir = './'

    with open(makefile_path, 'r') as file:
        lines = file.readlines()

    variables = ['NAME', 'SRC', 'HEADER']
    updated_lines = []
    for line in lines:
        for variable in variables:
            if line.startswith(variable):
                updated_line = line.strip()
                if variable == 'NAME':
                    updated_line += ' ' + project_info.get('proj_name', '') + '\n'
                elif variable == 'SRC':
                    updated_line += ' ' + project_info.get('file_name', '') + '\n'
                elif variable == 'HEADER':
                    updated_line += ' ' + project_info.get('h_files', '') + '\n'
                updated_lines.append(updated_line)
                break
        else:
            updated_lines.append(line)

    output_file = os.path.join(output_dir, os.path.basename(makefile_path))
    with open(output_file, 'w') as file:
        file.writelines(updated_lines)




def create_cpp_class(project_info):
    i = 1

    need_makefile = input("Do you need a Class? (y/n): ").lower() == "y"
    if need_makefile:
        num_files = int(input("\nEnter the number of Classes you need in the project"))
        while i <= num_files:
            class_name = input("Enter the name of the C++ Class: ")
            header_file = class_name + ".hpp"
            project_info['class_h_files'] += header_file
            source_file = class_name + ".cpp"
            project_info['class_src_files'] += source_file
            file = open(f"./{project_info['proj_name']}/includes/{header_file}", "x")
            file = open(f"./{project_info['proj_name']}/src/{source_file}", "x")
            i += 1

def create_project_basics(project_info):
    i = 1

    os.makedirs(project_info['proj_name'])
    os.makedirs(f"./{project_info['proj_name']}/src")
    os.makedirs(f"./{project_info['proj_name']}/includes")
    print("\nEnter the number of source files needed in the project")
    num_files = int(input("(You can create the files for you classes later!):"))
    project_info['num_src_files'] = num_files
    exec_names = []

    name = project_info['file_name']
    while i <= num_files:
        file_name = input(f"Enter the file name (without extension) for file {i}: ")
        if language == "python":
            file_name += ".py"
        elif language == "c":
            file_name += ".c"
        elif language == "cpp" or language == "c++":
            file_name += ".cpp"
        name += file_name
        file = open(f"./{project_info['proj_name']}/src/{file_name}", "x")
        i += 1

def create_makefile(project_info):
    need_makefile = input("Do you need a Makefile? (y/n): ").lower() == "y"
    if need_makefile:
        file = open(f"./{project_info['proj_name']}/Makefile", "x")
        insert_makefile_content(project_info)

def create_header_files(project_info):
    i = 1

    print("\nEnter the number of header files needed in the project")
    num_files = int(input("(You can create the header files for you classes later!):"))
    while i <= num_files:
        file_name = input(f"Enter the file name (without extension) for file {i}: ")
        file_name += ".h"
        project_info['h_files'] += file_name
        file = open(f"./{project_info['proj_name']}/includes/{file_name}", "x")
        i += 1

# def create_py_project():
#     create_project_basics("python")
#     print("create python project")

def create_cpp_project(project_info):
    project_name = input("Enter the name of the project: ")
    project_info['proj_name'] = project_name
    create_project_basics(project_info)
    create_header_files(project_info)
    create_makefile(project_info)
    create_cpp_class(project_info)

# def create_c_project():
#     create_project_basics("c++")
#     print("create c project")


project_info = {'file_name': '', 'h_files': '', 'class_h_files': '', 'class_src_files': ''}
while True:
    language = input("Enter the programming language (c, c++, python): ")

    if language == "c++":
        project_info['pro_lang'] = "c++"
        create_cpp_project(project_info)
        break
    # elif language == "c++":
    #     create_cpp_project()
    #     break
    # elif language == "python":
    #     create_py_project()
    #     break
    else:
        print("Invalid input. Please try again.")
