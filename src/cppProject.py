from data import projectData
from gitHub import gitHub
from makefile import makefile
from basicStructure import basic
import os

class cppProject(gitHub, makefile, basic):
	def __init__(self, projectD: projectData):
		self.projectD  = projectD

	def createProject(self):
		if (self.projectD.gitRepo == "y"):
			if(self.createGitRepo() == False):
				exit()
		else:
			self.createProjectDirectory()
		self.createSourceCodeFiles()
		self.createHeaderFiles()
		self.createReadme()
		# self.selfcreateDocumentation()
		self.createGitignore()
		self.createClasses()
		self.createMakefile()
		self.modifyTemplateCppFile()
		self.modifyTemplateHeaderFile()
		self.modifyTemplateMakefile()
		if (self.projectD.gitRepo == "y"):
			self.pushToGitRepo()

	# create the source code files
	def createSourceCodeFiles(self):
		src_directory = f"./{self.projectD.projectName}/src"
		if not os.path.exists(src_directory):
			os.mkdir(src_directory)
		for i in range(self.projectD.amountSourceCodeFiles):
			file_path = f"{src_directory}/{self.projectD.nameSourceCodeFiles[i]}.cpp"
			file = open(file_path, "w+")
			if (self.projectD.nameSourceCodeFiles[i] == "main"):
				with open(file_path, "w") as file:
					file.write("#include <iostream>\n\nint main(int argc, char* argv[]) {\n\n\treturn 0;\n}\n")

			file.close()

	# create the header files
	def createHeaderFiles(self):
		includesDirectory = f"./{self.projectD.projectName}/include"
		if not os.path.exists(includesDirectory):
			os.mkdir(includesDirectory)
		for i in range(self.projectD.amountHeaderfiles):
			file = open(f"./{self.projectD.projectName}/include/{self.projectD.namesHeaderfiles[i]}.h", "w+")
			file.close()

	# modify template cpp file
	def modifyTemplateCppFile(self):
		script_dir = os.path.dirname(os.path.realpath(__file__))
		template_path = os.path.join(script_dir, "../templets/cppClassTemp/srcFileTemp/cppSrcTemp.cpp")
		for i in range(self.projectD.amountClasses):
			with open(template_path, "r") as file:
				data = file.read()
			modifiedTemplate = data.replace("Xxx", self.projectD.classNames[i])
			modifiedTemplate = modifiedTemplate.replace("XXX", self.projectD.classNames[i].upper())
			with open(f"./{self.projectD.projectName}/src/{self.projectD.classNames[i]}.cpp", "w") as file:
				file.write(modifiedTemplate)

	# modify template header file
	def modifyTemplateHeaderFile(self):
		script_dir = os.path.dirname(os.path.realpath(__file__))
		template_path = os.path.join(script_dir, "../templets/cppClassTemp/headerTemp/HeaderTemp.h")

		for i in range(self.projectD.amountClasses):
			with open(template_path, "r") as file:
				data = file.read()
			modifiedTemplate = data.replace("Xxx", self.projectD.classNames[i])
			modifiedTemplate = modifiedTemplate.replace("XXX", self.projectD.classNames[i].upper())
			with open(f"./{self.projectD.projectName}/include/{self.projectD.classNames[i]}.h", "w") as file:
				file.write(modifiedTemplate)