import sys
from cx_Freeze import setup, Executable

program_name = "Clipboard Manager"

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     program_name,           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]launcher.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

build_exe_options = {"packages": ["Pyside2", "pyperclip", "keyboard"],
                     "excludes": ["tkinter"],
                     "include_files": ["icon/", "icon.png"],
                     "include_msvcr": True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = program_name,
        version = "1.0.0",
        description = "",
        options = {"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
        executables = [Executable("clipboard_manager.py", base=base,)])