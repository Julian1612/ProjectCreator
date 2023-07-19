import os
import json
import requests
from data import projectData
from termcolor import colored

class gitHub:
	def __init__(self, projectD: projectData):
		self.projectD  = projectD

	# create git repo
	def pushToGitRepo(self):
		os.chdir(f"./{self.projectD.projectName}")
		os.system("git add .")
		os.system("git commit -m \"Initial commit\"")
		os.system("git push")

	# Regular expression pattern to match GitHub access token format
	def is_valid_access_token(self, personal_access_token):
		if (len(personal_access_token) != 40):
			return False
		return True

	def addAccessToken(self):
		print("Please add your GitHub access token")
		while True:
			try:
				personal_access_token = input("Enter your access token: ")
				if self.is_valid_access_token(personal_access_token):
					break
				else:
					print("Invalid access token format. Please try again.")
			except Exception as e:
				print(f"Error: {e}")
		script_dir = os.path.dirname(os.path.realpath(__file__))
		configPath = os.path.join(script_dir, "../config.json")
		try:
			with open(configPath) as config_file:
				config = json.load(config_file)
				config["access_token"] = personal_access_token
			with open(configPath, "w") as config_file:
				json.dump(config, config_file)
			print(colored("Access token added successfully!", "green"))
		except Exception as e:
			print(f"Error: {e}")


	def createGitRepo(self):
		if self.projectD.getAccessToken() == "":
			self.addAccessToken()
		personal_access_token = self.projectD.getAccessToken()
		api_base_url = "https://api.github.com"
		data = {
			"name": self.projectD.projectName,
			"description": self.projectD.repoDescription,
			"private": False
		}
		response = requests.post(f"{api_base_url}/user/repos", json=data, headers={
			"Authorization": f"Bearer {personal_access_token}"})
		if response.status_code == 201:
			repo_data = response.json()
			clone_url = repo_data["clone_url"]
			print(colored("Successfully created repository", "green"))
			os.system("git init")
			os.system(f"git clone {clone_url}")
			print(colored("Successfully cloned repository", "green"))
			return True
		else:
			self.addAccessToken()
			print(colored("Failed to create repository", "red"))
			print(colored("Try to add a valid GitHub access token", "red"))
			return False
