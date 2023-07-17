from data import Info
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
# create the source code files
def createSourceCodeFiles():
	src_directory = f"./{info.projectName}/src"

	# Create the src directory if it doesn't exist
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

# 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
# create git repo
def pushToGitRepo():
	os.chdir(f"./{info.projectName}")
	os.system("git add .")
	os.system("git commit -m \"Initial commit\"")
	os.system("git push")

# add acces token
def addAccesToken():
	print("Please add your github acces token")
	personal_access_token = input("Enter your acces token: ")
	script_dir = os.path.dirname(os.path.realpath(__file__))
	configPath = os.path.join(script_dir, "../config.json")
	with open(configPath) as config_file:
		config = json.load(config_file)
		config["access_token"] = personal_access_token
	with open(configPath, "w") as config_file:
		json.dump(config, config_file)

def createGitRepo():
	if info.getAccesToken() == "":
		addAccesToken()
	personal_access_token = info.getAccesToken()
	api_base_url = "https://api.github.com"
	data = {
		"name": info.projectName,
		"description": info.repoDescription,
		"private": False
	}
	response = requests.post(f"{api_base_url}/user/repos", json=data, headers={
		"Authorization": f"Bearer {personal_access_token}"
	})
	if response.status_code == 201:
		repo_data = response.json()
		clone_url = repo_data["clone_url"]
		print("Successfully created repository")
		print(f"Clone URL: {clone_url}")
	else:
		print("Failed to create repository")
	os.system("git init")
	os.system(f"git clone {clone_url}")

info = Info()
print(info.gitRepo)
if (info.gitRepo == "y"):
	createGitRepo()
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
if (info.gitRepo == "y"):
	pushToGitRepo()
