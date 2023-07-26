from data import projectData
from cppProject import cppProject

dataProject = projectData(False)
if (dataProject.language == "cpp"):
	cppProject = cppProject(dataProject)
	cppProject.createClasses()
	cppProject.modifyTemplateCppFile()
	cppProject.modifyTemplateHeaderFile()
