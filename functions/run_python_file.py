import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    current_path = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not absolute_path.startswith(current_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python3", absolute_path], capture_output=True, timeout=30)
        if result:
            output = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
            if result.returncode != 0:
                output += f"\nProcess exited with code {result.returncode}"
            return output
        return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run executable python files and displays the stdout, stderr, and return code (if not 0), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the executable file, relative to the working directory. Will only execute if file has '.py' extension",
            ),
        },
    ),
)