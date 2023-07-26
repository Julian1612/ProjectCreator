#!/bin/bash

# Get the current directory containing the script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

printf "%s" "$script_dir"

# Create the alias line with the dynamic path
alias_line="alias create='python3 $script_dir/src/main.py'"
zshrc_file="$HOME/.zshrc"

# Check if the shell is Zsh
if [ "$(basename "$SHELL")" != "zsh" ]; then
    echo "This script is meant to be used with Zsh. Please switch to Zsh and run the script again."
    exit 1
fi

# Check if the alias already exists in .zshrc
if grep -Fxq "$alias_line" "$zshrc_file"; then
    echo "Alias already exists in .zshrc."
else
    # Add the alias to .zshrc
    echo "$alias_line" >> "$zshrc_file"
    echo "Alias added to .zshrc."
fi

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it before continuing."
    exit 1
fi

# Install dependencies in a virtual environment (recommended)
project_dir="$script_dir"
venv_dir="$project_dir/venv"

# Create and activate the virtual environment
python3 -m venv "$venv_dir"
source "$venv_dir/bin/activate"

# Install dependencies inside the virtual environment
pip install PyGithub
pip install python-dotenv

# Deactivate the virtual environment
deactivate
