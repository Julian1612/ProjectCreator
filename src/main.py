from data import projectData
from cppProject import cppProject
from cProject import cProject

#@todo makefile fur c projecte werden noch nicht richtig erstellt
projectD = projectData()
if (projectD.language == "cpp"):
	cppProject = cppProject(projectD)
	cppProject.createProject()
if (projectD.language == "c"):
	cProject = cProject(projectD)
	cProject.createProject()
