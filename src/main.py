from data import projectData
from cppProject import cppProject
from cProject import cProject
from pythonProject import pythonProject

projectD = projectData(True)
if (projectD.language == "cpp" or
	projectD.language == "c++" or
	projectD.language == "C++"):
	try:
		cppProject = cppProject(projectD)
		cppProject.createProject()
	except:
		print("\033[91m-------------------------------------------------------")
		print("Error 1")
		print("Sorry something went wrong. Please try again.")
		print("If the problem persists please open an issue on GitHub.")
		print("-------------------------------------------------------\033[0m")
		exit()

elif (projectD.language == "C" or
	projectD.language == "c"):
	try:
		cProject = cProject(projectD)
		cProject.createProject()
	except:
		print("\033[91m-------------------------------------------------------")
		print("Error 2")
		print("Sorry something went wrong. Please try again.")
		print("If the problem persists please open an issue on GitHub.")
		print("-------------------------------------------------------\033[0m")
		exit()
elif (projectD.language == "python" or
	projectD.language == "Python"):
	# try:
	pythonProject = pythonProject(projectD)
	pythonProject.createProject()
	# except:
	# 	print("\033[91m-------------------------------------------------------")
	# 	print("Error 3")
	# 	print("Sorry something went wrong. Please try again.")
	# 	print("If the problem persists please open an issue on GitHub.")
	# 	print("-------------------------------------------------------\033[0m")
	# 	exit()
