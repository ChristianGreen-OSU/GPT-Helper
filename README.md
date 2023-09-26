# GPT-Helper
A python script to easily paste relevant labeled files into chat gpt so that it can best help you with your code project.

# README

## Code File Combiner

The Code File Combiner is a Python application that combines the contents of selected code files within a chosen directory. The application is built on the Tkinter library, providing a simple graphical user interface for ease of use.

The application imports a list of code file extensions from a `config.py` file, and uses this to determine which files in a directory should be considered "code files". It then provides checkboxes for each file found, allowing the user to select which files' contents should be combined. The combined contents are displayed in a text box within the application.

## Getting Started

## 🏮‼️Update: All you need to do now is download the executable and run it!🏮‼️ (I hope)

To get the Code File Combiner working on your machine, you will need to have Python installed. This application was developed using Python 3.9 but should work with Python 3.6 and newer. 

You will also need the Tkinter library, which is included with standard Python distributions. If you're using a minimal Python installation, you may need to install Tkinter manually.

### Step 1: Clone the Repository

The green code button on the main page is a great place to start!

### Step 2: Setup the Configuration File

The application requires a `config.py` file in the same directory as the main application file. The `config.py` file should define a list variable `CODE_EXTENSIONS` that contains the file extensions of the types of code files you want the application to recognize.

Here's a sample `config.py`:

```python
CODE_EXTENSIONS = ['.py', '.js', '.java', '.c', '.cpp', '.cs', '.rb', '.go', '.php']
```

This configuration will cause the application to recognize Python, JavaScript, Java, C, C++, C#, Ruby, Go, and PHP files as "code files".

### Step 3: Run the Application

From the terminal, navigate to the directory that contains the Code File Combiner application files and run the application:

```
python3 gui_main.py
```
or
```
py -3 gui_main.py
```
This will launch the Tkinter application window.

If you want to just use the text interface, you'll have to edit lines with in the code for your own use. It's not recommended except for very occasional use. To run it you would run the same commands as above, just without 'gui_' in the file name.

### Step 4: Using the Application

1. Click the "Browse" button to select a directory that contains code files.
2. Once a directory is selected, checkboxes will appear for each code file found in the directory.
3. Select the checkboxes for the files whose contents you want to combine.
4. Click the "Process" button to combine the selected files.
5. The combined content of the selected files will appear in the text box.

That's it! You're ready to use the Code File Combiner.

## Troubleshooting

If you experience any issues while using the Code File Combiner, ensure you have the correct Python version installed and that the Tkinter library is available.

Also, make sure that your `config.py` file is set up correctly and is in the same directory as the main application file. If you've made any changes to the configuration, you will need to restart the application for the changes to take effect.
