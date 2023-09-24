from data import projectData
import os
import subprocess
from cppProject import cppProject
from cProject import cProject
from pythonProject import pythonProject

def searchForUpdates():
	repository_url = "https://github.com/Julian1612/ProjectCreator.git"
	local_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(local_directory)
	current_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")
	subprocess.run(["git", "fetch"])
	compare_output = subprocess.check_output(["git", "rev-list", "--left-right", f"{current_branch}...origin/{current_branch}"]).strip().decode("utf-8")
	if compare_output:
		print("Local branch is behind. Pulling the latest changes...")
		subprocess.run(["git", "pull"])
		print("\033[32mUpdate complete.\033[0m")

searchForUpdates()
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
	try:
		pythonProject = pythonProject(projectD)
		pythonProject.createProject()
	except:
		print("\033[91m-------------------------------------------------------")
		print("Error 3")
		print("Sorry something went wrong. Please try again.")
		print("If the problem persists please open an issue on GitHub.")
		print("-------------------------------------------------------\033[0m")
		exit()
