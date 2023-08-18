"""
PyInstaller is a tool that allows you to package Python programs as standalone executables. It takes your Python code
along with its dependencies and creates a self-contained executable that can be run on a target system without needing
a Python interpreter or any additional dependencies installed.

console – pip install pyinstaller
now get to the directory with your .py script (cd dirname или cd ..)
console – pyinstaller your_script.py

This will create your_script.exe on Windows, and probably some other executable, if pyinstaller is executed on Linux.
There also would be some extra files and folders, that represents Python's libraries, that were used in your initial
your_script.py. So, if you want to move this exe to some other place, you need to take all the that files with you.
"""