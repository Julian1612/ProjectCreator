from data import projectData
from cppProject import cppProject
from cProject import cProject
from pythonProject import pythonProject

#@todo makefile fur c projecte werden noch nicht richtig erstellt
#@todo make it to choose if the git repo is private or public
projectD = projectData(True)
if (projectD.language == "cpp"):
	cppProject = cppProject(projectD)
	cppProject.createProject()
elif (projectD.language == "c"):
	cProject = cProject(projectD)
	cProject.createProject()
elif (projectD.language == "python"):
	pythonProject = pythonProject(projectD)
	pythonProject.createProject()
