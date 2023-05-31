import os

def write_variables(makefile_path, output_dir, new_values):
    with open(makefile_path, 'r') as file:
        lines = file.readlines()

    variables = ['NAME', 'SRC', 'HEADER']
    updated_lines = []
    for line in lines:
        for variable in variables:
            if line.startswith(variable):
                updated_line = line.strip()
                updated_line += ' ' + new_values.get(variable, '') + '\n'
                updated_lines.append(updated_line)
                break
        else:
            updated_lines.append(line)

    output_file = os.path.join(output_dir, os.path.basename(makefile_path))
    with open(output_file, 'w') as file:
        file.writelines(updated_lines)


# Example usage
makefile_path = './templets/makefile/Makefile'
output_dir = './'
new_values = {'NAME': 'Test', 'SRC': 'test.cpp lol.cpp', 'HEADER': 'test.hpp lol.hpp'}
write_variables(makefile_path, output_dir, new_values)
