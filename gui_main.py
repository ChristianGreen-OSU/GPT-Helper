import os
import tkinter as tk
from tkinter import filedialog
# Import the CODE_EXTENSIONS variable
from config import CODE_EXTENSIONS

# Determine if a file has an extension matching those in the CODE_EXTENSIONS list
def is_code_file(file_name):
    return any(file_name.endswith(extension) for extension in CODE_EXTENSIONS)

# List all relevant files with matching extensions in the provided code directory
def list_relevant_files(code_directory):
    relevant_files = []

    for root, _, files in os.walk(code_directory):
        for file_name in files:
            if is_code_file(file_name):
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, code_directory)
                relevant_files.append(relative_path)

    return relevant_files

# Combine the content of the selected code files
def combine_code_files(code_directory, selected_files):
    combined_text = ""

    for file in selected_files:
        file_path = os.path.join(code_directory, file)
        combined_text += f"File: {file}\n"
        combined_text += "=====================================\n"

        with open(file_path, 'r') as infile:
            combined_text += infile.read()
            combined_text += "\n\n"

    return combined_text

# Open a directory selection dialog and update the directory entry field and file checkboxes
def browse_directory():
    directory = filedialog.askdirectory()
    code_directory_entry.delete(0, tk.END)
    code_directory_entry.insert(0, directory)

    update_file_checkboxes(directory)

# Update the file checkboxes based on the selected directory
def update_file_checkboxes(directory):
    relevant_files = list_relevant_files(directory)

    for widget in file_checkboxes_frame.winfo_children():
        widget.destroy()

    for file in relevant_files:
        var = tk.BooleanVar(value=True)
        checkbox = tk.Checkbutton(file_checkboxes_frame, text=file, variable=var, onvalue=True, offvalue=False)
        checkbox.var = var
        checkbox.pack(anchor=tk.W)

# Process the selected directory, combining the content of the selected files
def process_directory():
    code_directory = code_directory_entry.get()

    selected_files = [
        checkbox.cget("text")
        for checkbox in file_checkboxes_frame.winfo_children()
        if checkbox.var.get()
    ]

    combined_text = combine_code_files(code_directory, selected_files)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, combined_text)


# Create the Tkinter window
window = tk.Tk()
window.title("Code File Combiner")

# Create widgets
code_directory_label = tk.Label(window, text="Code Directory:")
code_directory_entry = tk.Entry(window, width=50)
browse_button = tk.Button(window, text="Browse", command=browse_directory)
process_button = tk.Button(window, text="Process", command=process_directory)
file_checkboxes_frame = tk.Frame(window)
output_text = tk.Text(window, wrap=tk.WORD)
scrollbar = tk.Scrollbar(window, command=output_text.yview)

# Configure text box to use scrollbar
output_text.configure(yscrollcommand=scrollbar.set)

# Place widgets
code_directory_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
code_directory_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
browse_button.grid(row=0, column=2, padx=5, pady=5)
process_button.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
file_checkboxes_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=3, sticky=tk.W+tk.E)
output_text.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)
scrollbar.grid(row=3, column=2, padx=5, pady=5, sticky=tk.N+tk.S)

# Configure grid weights
window.columnconfigure(1, weight=1)
window.rowconfigure(3, weight=1)

# Run the Tkinter event loop
window.mainloop()

