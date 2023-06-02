# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jschneid <jschneid@student.42heilbronn.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/31 15:55:12 by jschneid          #+#    #+#              #
#    Updated: 2023/06/02 17:32:46 by jschneid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import shutil
import time

def insert_makefile_content(project_info):
    makefile_path = './templets/makefile/Makefile'
    output_dir = f"./{project_info['name']}"

    with open(makefile_path, 'r') as file:
        lines = file.readlines()

    variables = ['NAME', 'SRC', 'HEADER']
    updated_lines = []
    for line in lines:
        for variable in variables:
            if line.startswith(variable):
                if variable == 'NAME':
                    updated_line = variable + '     = ' + project_info.get('name', '') + '\n'
                elif variable == 'SRC':
                    src_files = ' '.join(project_info.get('src_files', []))
                    updated_line = variable + '      = ' + src_files + '\n'
                elif variable == 'HEADER':
                    header_files = ' '.join(project_info.get('h_files', []))
                    updated_line = variable + '   = ' + header_files + '\n'
                break
        else:
            updated_line = line
        updated_lines.append(updated_line)

    output_file = os.path.join(output_dir, os.path.basename(makefile_path))
    with open(output_file, 'w') as file:
        file.writelines(updated_lines)

def create_cpp_class(project_info):
    i = 1

    need_makefile = input("Do you need a Class? (y/n): ").lower() == "y"
    if need_makefile:
        num_files = int(input("\nEnter the number of Classes you need in the project: "))
        while i <= num_files:
            j = 1
            class_name = input("Enter the name of the C++ Class: ")
            header_file = class_name + ".hpp"
            project_info['h_files'].append(header_file)
            source_file = class_name + ".cpp"
            project_info['src_files'].append(source_file)

            project_info[f"class_vars_{i}"] = []
            need_var = input("Do you want to add variables to the class? (y/n): ").lower() == "y"
            if need_var:
                num_var = int(input("\nEnter the number of variables you need in the class: "))
                while j <= num_var:
                    var_name = input("Enter the name of the variable: ")
                    var_specifier = input("In which specifier is the variable? (1/2/3): ")
                    if (var_specifier == "1"):
                        project_info[f"class_vars{i}"].append(var_name)
# hier jetzt noch spezifizieren ob 1 2 oder 3, dann fur jede class die
# erstellt werden soll einen eigenen key im dictionary erstellen (sub dictionary)
# {'class_n':{
        # 'private': ['var1', 'var2', 'var3']
        # 'protected' ...
# }
# }
                    j += 1


            # Create the header file
            header_content = f"#ifndef {class_name.upper()}_HPP\n"
            header_content += f"#define {class_name.upper()}_HPP\n\n"
            header_content += f"class {class_name} {{\n"
            header_content += " public:\n"
            header_content += "  // Constructor\n"
            header_content += f"  {class_name}(void);\n"
            header_content += f"  {class_name}(const {class_name}& obj);\n"
            header_content += "  // Destructor\n"
            header_content += f"  ~{class_name}(void);\n"
            header_content += "  // Operators\n"
            header_content += f"  {class_name} &operator=(const {class_name} &assign)\n"

            header_content += "};\n\n"
            header_content += f"#endif // {class_name.upper()}_HPP\n"

            with open(f"./{project_info['name']}/includes/{header_file}", "w") as file:
                file.write(header_content)

            # Create the source file
            source_content = f'#include "{header_file}"\n\n'
            source_content += f"{class_name}::{class_name}() {{\n"
            source_content += "    // Implement the constructor here\n"
            source_content += "}\n"

            with open(f"./{project_info['name']}/src/{source_file}", "w") as file:
                file.write(source_content)

            i += 1


def create_project_basics(project_info):
    i = 1

    os.makedirs(project_info['name'])
    os.makedirs(f"./{project_info['name']}/src")
    os.makedirs(f"./{project_info['name']}/includes")
    print("\nEnter the number of source files needed in the project")
    num_files = int(input("(You can create the files for you classes later!): "))
    project_info['num_src_files'] = num_files
    project_info['src_files'] = []
    while i <= num_files:
        src_files = input(f"Enter the file name (without extension) for file {i}: ")
        if language == "python":
            src_files += ".py"
        elif language == "c":
            src_files += ".c"
        elif language == "cpp" or language == "c++":
            src_files += ".cpp"
        project_info['src_files'].append(src_files)
        file = open(f"./{project_info['name']}/src/{src_files}", "x")
        i += 1

def create_makefile(project_info):
    need_makefile = input("Do you need a Makefile? (y/n): ").lower() == "y"
    if need_makefile:
        file = open(f"./{project_info['name']}/Makefile", "x")
        insert_makefile_content(project_info)

def create_header_files(project_info):
    i = 1

    print("\nEnter the number of header files needed in the project")
    num_files = int(input("(You can create the header files for you classes later!): "))
    project_info['h_files'] = []
    while i <= num_files:
        src_files = input(f"Enter the file name (without extension) for file {i}: ")
        src_files += ".h"
        project_info['h_files'].append(src_files)
        file = open(f"./{project_info['name']}/includes/{src_files}", "x")
        i += 1

# def create_py_project():
#     create_project_basics("python")
#     print("create python project")

def create_cpp_project(project_info):
    project_name = input("Enter the name of the project: ")
    project_info['name'] = project_name
    create_project_basics(project_info)
    create_header_files(project_info)
    create_cpp_class(project_info)
    # create_makefile(project_info)

# def create_c_project():
#     create_project_basics("c++")
#     print("create c project")


project_info = {'src_files': '', 'h_files': ''}
while True:
    language = input("Enter the programming language (c, c++, python): ")

    if language == "c++":
        project_info['language'] = "c++"
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
print(project_info)
