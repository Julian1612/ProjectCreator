from data import projectData
from cppProject import cppProject

projectD = projectData()
if (projectD.language == "cpp"):
	cppProject = cppProject(projectD)
	cppProject.createProject()
