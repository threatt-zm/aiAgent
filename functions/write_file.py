import os
from google.genai import types

def write_file(working_directory, file_path, content=""):
    current_path = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not absolute_path.startswith(current_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(absolute_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="overwrites the contents of the specified file with the contents provided, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory. If it doesn't exist, then it will be created.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file. If not provided, the file will be cleared"
            ),
        },
    ),
)