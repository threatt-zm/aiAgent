import os

def get_files_info(working_directory, directory=None):
    current_path = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(relative_path)
    
    if not directory.startswith("."):
        if directory not in os.listdir(current_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
        elif not os.path.isdir(absolute_path):
            return f'Error: "{directory}" is not a directory\n'
    
    print(f"Contents of working directory {relative_path}:")
    try:
        contents = ""
        for content in os.listdir(absolute_path):
            file_path = os.path.join(absolute_path, content)
            contents += f"- {content}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        return contents
    except Exception as e:
        return f"Error: {e}"

