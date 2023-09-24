from data import projectData
from gitHub import gitHub
from makefile import makefile
from basicStructure import basic
import os

class cProject(gitHub, makefile, basic):
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
		self.createMakefile()
		self.modifyTemplateHeaderFile()
		# self.modifyTemplateMakefile()
		if (self.projectD.gitRepo == "y"):
			self.pushToGitRepo()

	# create the source code files
	def createSourceCodeFiles(self):
		src_directory = f"./{self.projectD.projectName}/src"
		if not os.path.exists(src_directory):
			os.mkdir(src_directory)
		for i in range(self.projectD.amountSourceCodeFiles):
			file_path = f"{src_directory}/{self.projectD.nameSourceCodeFiles[i]}.c"
			file = open(file_path, "w+")
			if (self.projectD.nameSourceCodeFiles[i] == "main"):
				with open(file_path, "w") as file:
					file.write("#include <unistd.h>\n\nint main(int argc, char* argv[]) {\n\n\treturn 0;\n}\n")
			file.close()

	# create the header files
	def createHeaderFiles(self):
		includesDirectory = f"./{self.projectD.projectName}/includes"
		if not os.path.exists(includesDirectory):
			os.mkdir(includesDirectory)
		for i in range(self.projectD.amountHeaderfiles):
			file = open(f"./{self.projectD.projectName}/includes/{self.projectD.namesHeaderfiles[i]}.h", "w+")
			file.close()

	# modify template header file
	def modifyTemplateHeaderFile(self):
		script_dir = os.path.dirname(os.path.realpath(__file__))
		template_path = os.path.join(script_dir, "../templets/cTemp/headerfile.h")
		for i in range(self.projectD.amountHeaderfiles):
			with open(template_path, "r") as file:
				data = file.read()
			modifiedTemplate = data.replace("XXX", self.projectD.namesHeaderfiles[i].upper())
			with open(f"./{self.projectD.projectName}/includes/{self.projectD.namesHeaderfiles[i]}.h", "w") as file:
				file.write(modifiedTemplate)

