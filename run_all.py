import subprocess
import sys

print("Step 1: Data Acquisition & Joining")
subprocess.run([sys.executable, "join.py"], check=True)

print("Step 2: Exploratory Data Analysis")
subprocess.run([
    "jupyter", "nbconvert", "--to", "notebook",
    "--execute", "EDA.ipynb",
    "--output", "EDA.ipynb"
], check=True)

print("Step 3: Modeling")
subprocess.run([
    "jupyter", "nbconvert", "--to", "notebook",
    "--execute", "models_2.ipynb",
    "--output", "models_2.ipynb"
], check=True)

print("Finished running all steps")