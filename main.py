import os
import shutil
import time

def create_cpp_class(project_name):
    i = 1

    need_makefile = input("Do you need a Class? (y/n): ").lower() == "y"
    if need_makefile:
        num_files = int(input("\nEnter the number of Classes you need in the project"))
        while i <= num_files:
            class_name = input("Enter the name of the C++ Class: ")
            header_file = class_name + ".hpp"
            source_file = class_name + ".cpp"
            file = open(f"./{project_name}/includes/{header_file}", "x")
            file = open(f"./{project_name}/src/{source_file}", "x")
            i += 1

def create_project_basics(language, project_name):
    i = 1

    os.makedirs(project_name)
    os.makedirs(f"./{project_name}/src")
    os.makedirs(f"./{project_name}/includes")
    print("\nEnter the number of source files needed in the project")
    num_files = int(input("(You can create the files for you classes later!):"))

    file_names = []
    exec_names = []

    while i <= num_files:
        file_name = input(f"Enter the file name (without extension) for file {i}: ")
        if language == "python":
            file_name += ".py"
        elif language == "c":
            file_name += ".c"
        elif language == "cpp" or language == "c++":
            file_name += ".cpp"
        file = open(f"./{project_name}/src/{file_name}", "x")
        i += 1

def create_makefile(project_name):
    need_makefile = input("Do you need a Makefile? (y/n): ").lower() == "y"
    if need_makefile:
        file = open(f"./{project_name}/Makefile", "x")

def create_header_files(project_name):
    i = 1
    file_names = []
    exec_names = []

    print("\nEnter the number of header files needed in the project")
    num_files = int(input("(You can create the header files for you classes later!):"))
    while i <= num_files:
        file_name = input(f"Enter the file name (without extension) for file {i}: ")
        file_name += ".h"
        file = open(f"./{project_name}/includes/{file_name}", "x")
        i += 1

def create_py_project():
    create_project_basics("python")
    print("create python project")

def create_cpp_project():
    project_name = input("Enter the name of the project: ")
    create_project_basics("cpp", project_name)
    create_header_files(project_name)
    create_makefile(project_name)
    create_cpp_class(project_name)

def create_c_project():
    create_project_basics("c++")
    print("create c project")


while True:
    language = input("Enter the programming language (c, c++, python): ")

    if language == "c++":
        create_cpp_project()
        break
    # elif language == "c++":
    #     create_cpp_project()
    #     break
    # elif language == "python":
    #     create_py_project()
    #     break
    else:
        print("Invalid input. Please try again.")

