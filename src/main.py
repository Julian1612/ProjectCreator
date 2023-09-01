from data import projectData
from cppProject import cppProject
from cProject import cProject
from pythonProject import pythonProject

projectD = projectData(True)
if (projectD.language == "cpp",
	projectD.language == "c++",
	projectD.language == "C++"):
	cppProject = cppProject(projectD)
	cppProject.createProject()
elif (projectD.language == "C",
	projectD.language == "c"):
	cProject = cProject(projectD)
	cProject.createProject()
elif (projectD.language == "python",
	projectD.language == "Python"):
	pythonProject = pythonProject(projectD)
	pythonProject.createProject()
