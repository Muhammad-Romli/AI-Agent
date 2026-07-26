import os

def write_file(working_directory: str, file_path: str, content:str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, file_path_abs])
        is_valid_file_path = common_path == working_dir_abs

        if not is_valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        #this is the writing part
        file_path_abs_without_tail = os.path.dirname(file_path_abs)
        os.makedirs(file_path_abs_without_tail, exist_ok=True)
        with open(file_path_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: write_files module failed to run: {e}"


schema_write_file= {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write(overwriting) the content of a file located at the specified file path relative to the given working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the directory.",
                },
                "content" : {
                    "type": "string",
                    "description": "The content that gonna be written in the specified file",
                },
                "directory": {
                    "type": "string",
                    "description": "Directory path relative to the working directory (defaults to current working directory if omitted).",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
