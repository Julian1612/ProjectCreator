from data import Info
import os

# create the directory for the project
def createProjectDirectory():
	os.mkdir(f"./{info.projectName}")
	os.mkdir(f"./{info.projectName}/src")
	os.mkdir(f"./{info.projectName}/include")

# create the source code files
def createSourceCodeFiles():
	for i in range(info.amountSourceCodeFiles):
		file = open(f"./{info.projectName}/src/{info.nameSourceCodeFiles[i]}.cpp", "w+")
		if (info.nameSourceCodeFiles[i] == "main"):
			with open(f"./{info.projectName}/src/{info.nameSourceCodeFiles[i]}.cpp", "w") as file:
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
def createClasses():
	for i in range(info.amountClasses):
		file = open(f"./{info.projectName}/src/{info.classNames[i]}.cpp", "w+")
		file.close()
		file = open(f"./{info.projectName}/include/{info.classNames[i]}.h", "w+")
		file.close()

# create Makefile
def createMakefile():
	file = open(f"./{info.projectName}/Makefile", "w+")
	file.close()

# modify template cpp file
def modifyTemplateCppFile():
	for i in range(info.amountClasses):
		with open(f"../templets/cppClassTemp/srcFileTemp/cppSrcTemp.cpp", "r") as file:
			data = file.read()
		modifiedTemplate = data.replace("Xxx", info.classNames[i])
		modifiedTemplate = modifiedTemplate.replace("XXX", info.classNames[i].upper())
		with open(f"./{info.projectName}/src/{info.classNames[i]}.cpp", "w") as file:
			file.write(modifiedTemplate)

# modify template header file
def modifyTemplateHeaderFile():
	for i in range(info.amountClasses):
		with open(f"../templets/cppClassTemp/headerTemp/HeaderTemp.h", "r") as file:
			data = file.read()
		modifiedTemplate = data.replace("Xxx", info.classNames[i])
		modifiedTemplate = modifiedTemplate.replace("XXX", info.classNames[i].upper())
		with open(f"./{info.projectName}/include/{info.classNames[i]}.h", "w") as file:
			file.write(modifiedTemplate)

info = Info()
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
