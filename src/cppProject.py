from data import projectData
from gitHub import gitHub
from makefile import makefile
from basicStructure import basic
import os
import requests
import json

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

	@staticmethod
	def getRandomCodingJoke():
		url = "https://v2.jokeapi.dev/joke/programming?type=single"

		try:
			response = requests.get(url)
			if response.status_code == 200:
				jokeData = json.loads(response.text)
				joke = jokeData.get("joke")
				if '"' in joke:
					joke = joke.replace('"', '\\"')
				if '\n' in joke:
					joke = joke.repalce('\n', '\n\t')
				return joke
		except Exception as e:
			pass
		return "Hello World!"

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
					file.write("#include <iostream>\n")
					if (self.projectD.amountHeaderfiles > 0):
						for i in range(self.projectD.amountHeaderfiles):
							file.write(f"#include \"../includes/{self.projectD.namesHeaderfiles[i]}.h\"\n")
					if (self.projectD.amountClasses > 0):
						for i in range(self.projectD.amountClasses):
							file.write(f"#include \"../includes/{self.projectD.classNames[i]}.h\"\n")
					joke = cppProject.getRandomCodingJoke()
					file.write(f"\nint main(void) {{\n\tstd::cout << \"{joke}\" << std::endl;\n\treturn 0;\n}}\n")
			file.close()

	# create the header files
	def createHeaderFiles(self):
		includesDirectory = f"./{self.projectD.projectName}/includes"
		if not os.path.exists(includesDirectory):
			os.mkdir(includesDirectory)
		for i in range(self.projectD.amountHeaderfiles):
			file = open(f"./{self.projectD.projectName}/includes/{self.projectD.namesHeaderfiles[i]}.h", "w+")
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
			if (self.projectD.createClass == True):
				currentDir = os.getcwd()
				include_directory = f"{currentDir}/src"
				with open(f"{include_directory}/{self.projectD.classNames[i]}.cpp", "w") as file:
					file.write(modifiedTemplate)
			else:
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
			if (self.projectD.createClass == True):
				currentDir = os.getcwd()
				include_directory = f"{currentDir}/includes"
				with open(f"{include_directory}/{self.projectD.classNames[i]}.h", "w") as file:
					file.write(modifiedTemplate)
			else:
				with open(f"./{self.projectD.projectName}/includes/{self.projectD.classNames[i]}.h", "w") as file:
					file.write(modifiedTemplate)

	# create classes
	def createClasses(self):
		if self.projectD.createClass:
			currentDir = os.getcwd()
			src_directory = f"{currentDir}/src"
			include_directory = f"{currentDir}/includes"
		else:
			src_directory = f"./{self.projectD.projectName}/src"
			include_directory = f"./{self.projectD.projectName}/includes"
		if not os.path.exists(src_directory):
			os.mkdir(src_directory)
		if not os.path.exists(include_directory):
			os.mkdir(include_directory)
		for i in range(self.projectD.amountClasses):
			src_file_path = f"{src_directory}/{self.projectD.classNames[i]}.cpp"
			include_file_path = f"{include_directory}/{self.projectD.classNames[i]}.h"
			src_file = open(src_file_path, "w+")
			include_file = open(include_file_path, "w+")
			src_file.close()
			include_file.close()
