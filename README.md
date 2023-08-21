# ProjectCreator

Welcome to ProjectCreator! This is a useful tool to streamline your workflow and make project setup easier.

## Getting Started

Before you begin, make sure you have [Oh My Zsh](https://ohmyz.sh/) installed, as an alias will be created in the `.zshrc` file.

## Installation

### Clone this repository to your local machine:

Clone this repository to your local machine:

```bash
git clone https://github.com/Julian1612/ProjectCreator.git
```
### Navigate to the project directory:

```bash
cd ProjectCreator
```

### Run the install.sh script to add the necessary alias to your .zshrc file:

```bash
./install.sh
```
## How to use the tool
### Creating a New Project
To create a new project, follow these steps:

1. Open your terminal.

2. Navigate to the directory where you want to create the project.

Run the following command:

```bash
create
```
Follow the instructions provided to set up your new project.

### Creating a New Class
To create a new class, follow these steps:

1. Open your terminal.

2. Navigate to the directory of your project.

Run the following command:

```bash
class
```
Follow the instructions provided to create a new class within your project.

## Note for Non-Oh-My-Zsh Users
If you're not using Oh My Zsh, you'll need to manually add the alias. Open your shell configuration file (e.g., .bashrc, .bash_profile, or .zshrc) and add the following line:

```bash
alias create="path_to_the_main.py_from_this_project"
```

### Creating a GitHub Access Token
To interact with GitHub's API or perform actions on behalf of your account, you can create a personal access token:

1. Go to your GitHub account settings.
2. Under "Developer settings," select "Personal access tokens."
3. Click on "Generate new token."
4. Give your token a name and select the required permissions. For this project, public_repo scope might be sufficient.
5. Click "Generate token."
Remember to keep your access token secure and do not share it publicly.

# Contributing
Contributions are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request.
