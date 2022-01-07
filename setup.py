import sys
from cx_Freeze import setup, Executable

build_exe_options = {
"include_files" : ["plugins/"]
}

base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name = "Dash Desk Prototype",
    version = "0.1",
    description = "Dash Desk Prototype",
    options = {"build_exe": build_exe_options},
    executables = [Executable("home_index.py", base=base)]
)