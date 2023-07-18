from data import Info
from termcolor import colored
import requests
import os
import json

# create the directory for the project
def createProjectDirectory():
	print("Creating project directory")
	os.mkdir(f"./{info.projectName}")
	os.mkdir(f"./{info.projectName}/src")
	os.mkdir(f"./{info.projectName}/include")

# create the source code files
def createSourceCodeFiles():
	src_directory = f"./{info.projectName}/src"
	if not os.path.exists(src_directory):
		os.mkdir(src_directory)
	for i in range(info.amountSourceCodeFiles):
		file_path = f"{src_directory}/{info.nameSourceCodeFiles[i]}.cpp"
		file = open(file_path, "w+")
		if (info.nameSourceCodeFiles[i] == "main"):
			with open(file_path, "w") as file:
				file.write("#include <iostream>\n\nint main(int argc, char* argv[]) {\n\n\treturn 0;\n}\n")

		file.close()

# create the header files
def createHeaderFiles():
	includesDirectory = f"./{info.projectName}/include"
	if not os.path.exists(includesDirectory):
		os.mkdir(includesDirectory)
	for i in range(info.amountHeaderfiles):
		file = open(f"./{info.projectName}/include/{info.namesHeaderfiles[i]}.h", "w+")
		file.close()

# create the readme file
def createReadme():
	file = open(f"./{info.projectName}/README.md", "w+")
	file.close()

# create the documentation file
def createDocumentation():
	file = open(f"./{info.projectName}/documentation.md", "w+")
	file.close()

# create the gitignore file
def createGitignore():
	file = open(f"./{info.projectName}/.gitignore", "w+")
	with open(f"./{info.projectName}/.gitignore", "w") as file:
		file.write("./obj\n")
	file.close()

# create classes
def createClasses():
	src_directory = f"./{info.projectName}/src"
	include_directory = f"./{info.projectName}/include"

	# Create the src and include directories if they don't exist
	if not os.path.exists(src_directory):
		os.mkdir(src_directory)

	if not os.path.exists(include_directory):
		os.mkdir(include_directory)

	for i in range(info.amountClasses):
		src_file_path = f"{src_directory}/{info.classNames[i]}.cpp"
		include_file_path = f"{include_directory}/{info.classNames[i]}.h"

		src_file = open(src_file_path, "w+")
		include_file = open(include_file_path, "w+")

		src_file.close()
		include_file.close()


# create Makefile
def createMakefile():
	file = open(f"./{info.projectName}/Makefile", "w+")
	file.close()

# modify template cpp file
def modifyTemplateCppFile():
	script_dir = os.path.dirname(os.path.realpath(__file__))
	template_path = os.path.join(script_dir, "../templets/cppClassTemp/srcFileTemp/cppSrcTemp.cpp")
	for i in range(info.amountClasses):
		with open(template_path, "r") as file:
			data = file.read()
		modifiedTemplate = data.replace("Xxx", info.classNames[i])
		modifiedTemplate = modifiedTemplate.replace("XXX", info.classNames[i].upper())
		with open(f"./{info.projectName}/src/{info.classNames[i]}.cpp", "w") as file:
			file.write(modifiedTemplate)

# modify template header file
def modifyTemplateHeaderFile():
	script_dir = os.path.dirname(os.path.realpath(__file__))
	template_path = os.path.join(script_dir, "../templets/cppClassTemp/headerTemp/HeaderTemp.h")

	for i in range(info.amountClasses):
		with open(template_path, "r") as file:
			data = file.read()
		modifiedTemplate = data.replace("Xxx", info.classNames[i])
		modifiedTemplate = modifiedTemplate.replace("XXX", info.classNames[i].upper())
		with open(f"./{info.projectName}/include/{info.classNames[i]}.h", "w") as file:
			file.write(modifiedTemplate)

# create git repo
def pushToGitRepo():
	os.chdir(f"./{info.projectName}")
	os.system("git add .")
	os.system("git commit -m \"Initial commit\"")
	os.system("git push")

# Regular expression pattern to match GitHub access token format
def is_valid_access_token(token):
	if (len(token) != 40):
		return False
	return True

def addAccessToken():
    print("Please add your GitHub access token")
    while True:
        try:
            personal_access_token = input("Enter your access token: ")
            if is_valid_access_token(personal_access_token):
                break
            else:
                print("Invalid access token format. Please try again.")
        except Exception as e:
            print(f"Error: {e}")
    script_dir = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(script_dir, "../config.json")
    try:
        with open(configPath) as config_file:
            config = json.load(config_file)
            config["access_token"] = personal_access_token
        with open(configPath, "w") as config_file:
            json.dump(config, config_file)
        print(colored("Access token added successfully!", "green"))
    except Exception as e:
        print(f"Error: {e}")


def createGitRepo():
	if info.getAccessToken() == "":
		addAccessToken()
	personal_access_token = info.getAccessToken()
	api_base_url = "https://api.github.com"
	data = {
		"name": info.projectName,
		"description": info.repoDescription,
		"private": False
	}
	response = requests.post(f"{api_base_url}/user/repos", json=data, headers={
		"Authorization": f"Bearer {personal_access_token}"})
	if response.status_code == 201:
		repo_data = response.json()
		clone_url = repo_data["clone_url"]
		print(colored("Successfully created repository", "green"))
		os.system("git init")
		os.system(f"git clone {clone_url}")
		print(colored("Successfully cloned repository", "green"))
		return True
	else:
		addAccessToken()
		print(colored("Failed to create repository", "red"))
		print(colored("Try to add a valid GitHub access token", "red"))
		return False

def modifyTemplateMakefile():
	script_dir = os.path.dirname(os.path.realpath(__file__))
	template_path = os.path.join(script_dir, "../templets/Makefiles/makefileCppTemp.txt")
	with open(template_path, "r") as file:
		data = file.read()
	modifiedTemplate = data.replace("projectName", info.projectName)
	srcFiles = ""
	counter = 0
	for i in range(info.amountSourceCodeFiles):
		srcFiles += info.nameSourceCodeFiles[i] + ".cpp"
		srcFiles += " "
		if (counter == 5):
			srcFiles += "\\\n\t\t\t"
			counter = 0
		counter += 1
	for i in range(info.amountClasses):
		srcFiles += info.classNames[i] + ".cpp"
		srcFiles += " "
		if (counter == 5):
			srcFiles += "\\\n\t\t\t"
			counter = 0
		counter += 1
	modifiedTemplate = modifiedTemplate.replace("cppFiles...", srcFiles)
	headerfiles = ""
	counter = 0
	for i in range(info.amountHeaderfiles):
		headerfiles += info.namesHeaderfiles[i] + ".h"
		headerfiles += " "
		if (counter == 5):
			headerfiles += "\\\n\t\t\t"
			counter = 0
		counter += 1
	for i in range(info.amountClasses):
		headerfiles += info.classNames[i] + ".h"
		headerfiles += " "
		if (counter == 5):
			headerfiles += "\\\n\t\t\t"
			counter = 0
		counter += 1
	modifiedTemplate = modifiedTemplate.replace("hppFiles...", headerfiles)
	with open(f"./{info.projectName}/Makefile", "w") as file:
		file.write(modifiedTemplate)

#@todo wenn input the file names it should not be possible to enter a file name with a space
#@todo when input the file names it should not be possible to enter just a space
info = Info()
if (info.gitRepo == "y"):
	if(createGitRepo() == False):
		exit()
else:
	createProjectDirectory()
createSourceCodeFiles()
createHeaderFiles()
createReadme()
createDocumentation()
createGitignore()
createClasses()
createMakefile()
modifyTemplateCppFile()
modifyTemplateHeaderFile()
modifyTemplateMakefile()
if (info.gitRepo == "y"):
	pushToGitRepo()
