from data import projectData
import os

class basic:
	def __init__(self, projectD: projectData):
		self.projectD  = projectD

	# create the readme file
	def createReadme(self):
		file = open(f"./{self.projectD.projectName}/README.md", "w+")
		file.close()

#@todo checken ob ordner schon existiert sont error throwen
	# create the directory for the project
	def createProjectDirectory(self):
		print("Creating project directory")
		os.mkdir(f"./{self.projectD.projectName}")
		os.mkdir(f"./{self.projectD.projectName}/src")
		os.mkdir(f"./{self.projectD.projectName}/include")

	# create the documentation file
	def createDocumentation(self):
		file = open(f"./{self.projectD.projectName}/documentation.md", "w+")
		file.close()

	# create the gitignore file
	def createGitignore(self):
		file = open(f"./{self.projectD.projectName}/.gitignore", "w+")
		with open(f"./{self.projectD.projectName}/.gitignore", "w") as file:
			file.write("./obj\n")
		file.close()

	# create classes
	def createClasses(self):
		src_directory = f"./{self.projectD.projectName}/src"
		include_directory = f"./{self.projectD.projectName}/include"
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
