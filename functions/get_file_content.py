import os
from google.genai import types

def get_file_content(working_directory, file_path):
    current_path = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not absolute_path.startswith(current_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(absolute_path, "r") as f:
            file_content = f.read(10000)
            if os.path.getsize(absolute_path) > 10000:
                file_content += f'\n[...File "{file_path}" truncated at 10000 characters]'
            return file_content
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of the specified file constrained to the working directory, trucated if the size > 10000.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get the content from, relative to the working directory. File must exist in order to run.",
            ),
        },
    ),
)