class Info:
    def __init__(self):
        self.getProjectName()
        # self.getLanguage()
        self.getNumSourceCodeFiles()
        self.getNamesSourceCodeFiles(self.amountSourceCodeFiles)
        self.getNumHeaderfiles()
        self.getNamesHeaderfiles(self.amountHeaderfiles)
        self.getNumClasses()
        self.getClassName(self.amountClasses)

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

    def printUserInfo(self):
        print(self.projectName)
        print(self.language)
        print(self.amountSourceCodeFiles)
        print(self.nameSourceCodeFiles)
        print(self.amountHeaderfiles)
        print(self.namesHeaderfiles)
        print(self.amountClasses)
        print(self.classNames)
        print("Info initialized")

    projectName: str
    language: str
    amountSourceCodeFiles: int
    nameSourceCodeFiles: list
    amountHeaderfiles: int
    namesHeaderfiles: list
    amountClasses: int
    classNames: list
