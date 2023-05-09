import os
# Import the CODE_EXTENSIONS variable from the config module
from config import CODE_EXTENSIONS

# Specify the directory containing the code files
code_directory = r'C:\Users\green\Downloads\hw4_template'
output_file = 'combined_code_files.txt'

# Define a function to filter the desired code file extensions
def is_code_file(file_name):
    return any(file_name.endswith(extension) for extension in CODE_EXTENSIONS)

# Combine the contents of all code files into a single text file
with open(output_file, 'w') as outfile:
    # Iterate through the directory tree
    for root, _, files in os.walk(code_directory):
        # Iterate through each file in the directory
        for file_name in files:
            # Check if the file has an extension matching those in the CODE_EXTENSIONS list
            if is_code_file(file_name):
                # Construct the absolute and relative paths of the file
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, code_directory)
                
                # Write the file name and separator to the output file
                outfile.write(f"File: {relative_path}\n")
                outfile.write("=====================================\n")
                
                # Read the content of the file and write it to the output file
                with open(file_path, 'r') as infile:
                    outfile.write(infile.read())
                    # Add line breaks between files
                    outfile.write("\n\n")
