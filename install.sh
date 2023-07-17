#!/bin/bash

alias_line="alias ii='python3 ~/Project/src/main.py'"
zshrc_file="$HOME/.zshrc"

# Check if the alias already exists in .zshrc
if grep -Fxq "$alias_line" "$zshrc_file"; then
    echo "Alias already exists in .zshrc."
else
    # Add the alias to .zshrc
    echo "$alias_line" >> "$zshrc_file"
    echo "Alias added to .zshrc."
fi

# install dependencies
# install python3
pip3 install PyGithub python-dotenv

