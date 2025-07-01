import os
def write_file(working_directory, file_path, content):
    current_path = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not absolute_path.startswith(current_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        #if not os.path.exists(absolute_path):
        #    os.makedirs()
        with open(absolute_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"