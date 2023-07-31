from data import projectData
from gitHub import gitHub
from makefile import makefile
from basicStructure import basic
import os

class pythonProject(gitHub, makefile, basic):
	def __init__(self, projectD: projectData):
		self.projectD  = projectD

	def createProject(self):
		if (self.projectD.gitRepo == "y"):
			if(self.createGitRepo() == False):
				exit()
		else:
			self.createProjectDirectory()
		self.createSourceCodeFiles()
		self.createReadme()
		self.createGitignore()
		self.createClasses()
		self.createMakefile()
		self.modifyTemplatePythonFile()
		if (self.projectD.gitRepo == "y"):
			self.pushToGitRepo()

	def createSourceCodeFiles(self):
		src_directory = f"./{self.projectD.projectName}/src"
		if not os.path.exists(src_directory):
			os.mkdir(src_directory)
		for i in range(self.projectD.amountSourceCodeFiles):
			file_path = f"{src_directory}/{self.projectD.nameSourceCodeFiles[i]}.py"
			file = open(file_path, "w+")
			file.close()

	def modifyTemplatePythonFile(self):
		script_dir = os.path.dirname(os.path.realpath(__file__))
		template_path = os.path.join(script_dir, "../templets/pythonClassTemp/srcFileTemp/pythonSrcTemp.py")
		for i in range(self.projectD.amountClasses):
			with open(template_path, "r") as file:
				data = file.read()
			modifiedTemplate = data.replace("Xxx", self.projectD.classNames[i])
			file_path = f"./{self.projectD.projectName}/src/{self.projectD.classNames[i]}.py"
			with open(file_path, "w") as file:
				file.write(modifiedTemplate)


