import os
import json
from data import projectData

class makefile:
	def __init__(self, projectD: projectData):
		self.projectD  = projectD

	# create Makefile
	def createMakefile(self):
		file = open(f"./{self.projectD.projectName}/Makefile", "w+")
		file.close()

	def modifyTemplateMakefile(self):
		script_dir = os.path.dirname(os.path.realpath(__file__))
		template_path = os.path.join(script_dir, "../templets/Makefiles/makefileCppTemp.txt")
		with open(template_path, "r") as file:
			data = file.read()
		modifiedTemplate = data.replace("projectName", self.projectD.projectName)
		srcFiles = ""
		counter = 0
		for i in range(self.projectD.amountSourceCodeFiles):
			srcFiles += self.projectD.nameSourceCodeFiles[i] + ".cpp"
			srcFiles += " "
			if (counter == 5):
				srcFiles += "\\\n\t\t\t"
				counter = 0
			counter += 1
		for i in range(self.projectD.amountClasses):
			srcFiles += self.projectD.classNames[i] + ".cpp"
			srcFiles += " "
			if (counter == 5):
				srcFiles += "\\\n\t\t\t"
				counter = 0
			counter += 1
		modifiedTemplate = modifiedTemplate.replace("cppFiles...", srcFiles)
		headerfiles = ""
		counter = 0
		for i in range(self.projectD.amountHeaderfiles):
			headerfiles += self.projectD.namesHeaderfiles[i] + ".h"
			headerfiles += " "
			if (counter == 5):
				headerfiles += "\\\n\t\t\t"
				counter = 0
			counter += 1
		for i in range(self.projectD.amountClasses):
			headerfiles += self.projectD.classNames[i] + ".h"
			headerfiles += " "
			if (counter == 5):
				headerfiles += "\\\n\t\t\t"
				counter = 0
			counter += 1
		modifiedTemplate = modifiedTemplate.replace("hppFiles...", headerfiles)
		with open(f"./{self.projectD.projectName}/Makefile", "w") as file:
			file.write(modifiedTemplate)

