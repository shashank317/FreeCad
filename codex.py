# run_in_ide.py
import subprocess
from pathlib import Path

FREECAD_EXE = r"C:\Program Files\FreeCAD 1.0\bin\FreeCAD.exe"
SCRIPT = Path(__file__).with_name("claude2.py")  # or pully.py

subprocess.Popen([FREECAD_EXE, "--run-python-script", str(SCRIPT)])
