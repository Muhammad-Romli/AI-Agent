import os
import sys


#Below, is only fot importing from config
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir =  os.path.dirname(current_dir)
sys.path.append(parent_dir)
from config import max_chars #config.py is 1 level outside of this dictionary
#Above, is only fot importing from config


def get_file_content(working_directory:str, file_path:str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_path_abs])
        is_valid_path_file = common_path == working_dir_abs

        if not is_valid_path_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path_abs, "r") as f:
            file_content = f.read(max_chars)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {max_chars}]'
            return file_content

    except Exception as e:
        return f"Error: get_file_content module failed to run: {e}"





schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get the content of a file located at the specified file path relative to the given working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the directory.",
                },
                "directory": {
                    "type": "string",
                    "description": "Directory path relative to the working directory (defaults to current working directory if omitted).",
                },
            },
            "required": ["file_path"],
        },
    },
}
