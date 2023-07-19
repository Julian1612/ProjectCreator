import json
import os

class projectData:

    # Class variables
    gitRepo: str
    repoDescription: str
    accesToken: str
    projectName: str
    language: str
    amountSourceCodeFiles: int
    nameSourceCodeFiles: list
    amountHeaderfiles: int
    namesHeaderfiles: list
    amountClasses: int
    classNames: list

    # Constructor
    def __init__(self):
        self.getProjectName()
        self.getGitRepo()
        self.getLanguage()
        self.getNumSourceCodeFiles()
        self.getNamesSourceCodeFiles(self.amountSourceCodeFiles)
        self.getNumHeaderfiles()
        self.getNamesHeaderfiles(self.amountHeaderfiles)
        self.getNumClasses()
        self.getClassName(self.amountClasses)

    # Getters
    def getGitRepo(self):
        while True:
            self.gitRepo = input("You want to create a git repository (y/n): ")
            if self.gitRepo.lower() == 'y':
                break
            elif self.gitRepo.lower() == 'n':
                return
            else:
                print("Invalid input. Please try again.")
        while True:
            self.repoDescription = input("You want to add a description (y/n): ")
            if self.repoDescription.lower() == 'y':
                self.repoDescription = input("Enter the description: ")
                break
            elif self.repoDescription.lower() == 'n':
                break
            else:
                print("Invalid input. Please try again.")

    def getProjectName(self):
        while True:
            try:
                self.projectName = input("Enter the project name: ")
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def getLanguage(self):
        while True:
            try:
                self.language = input("Enter the programming language: ")
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def getNumSourceCodeFiles(self):
        while True:
            try:
                self.amountSourceCodeFiles = int(input("Enter the amount of source code files: "))
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def getNamesSourceCodeFiles(self, amount_files):
        self.nameSourceCodeFiles = []
        for i in range(amount_files):
            while True:
                try:
                    file_name = input(f"Enter the name of source code file {i+1}: ")
                    self.nameSourceCodeFiles.append(file_name)
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

    def getNumHeaderfiles(self):
        while True:
            try:
                self.amountHeaderfiles = int(input("Enter the amount of header files: "))
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def getNamesHeaderfiles(self, amount_files):
        self.namesHeaderfiles = []
        for i in range(amount_files):
            while True:
                try:
                    file_name = input(f"Enter the name of header file {i+1}: ")
                    self.namesHeaderfiles.append(file_name)
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

    def getNumClasses(self):
        while True:
            try:
                self.amountClasses = int(input("Enter the amount of classes: "))
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def getClassName(self, amount_classes):
        self.classNames = []
        for i in range(amount_classes):
            while True:
                try:
                    class_name = input(f"Enter the name of class {i+1}: ")
                    self.classNames.append(class_name)
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

    def getAccessToken(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(script_dir, "../config.json")

        if not os.path.exists(config_path):
            # Create the file if it doesn't exist
            with open(config_path, 'w') as config_file:
                config_file.write('{"access_token": ""}')

        with open(config_path) as config_file:
            config = json.load(config_file)
            self.accessToken = config["access_token"]
        return self.accessToken



