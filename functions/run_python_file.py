import subprocess
import os

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_path = os.path.join(working_dir_abs, file_path)
    file_path_abs = os.path.abspath(target_path)
    common_path = os.path.commonpath([working_dir_abs, file_path_abs])
    is_valid_file_path = common_path == working_dir_abs

    #This whole code block is error checks
    if not is_valid_file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path_abs):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", file_path_abs]
    if args is not None:
        command.extend(args)

    
    completed_process = subprocess.run(
        command, 
        cwd=working_dir_abs, 
        capture_output=True,
        text=True, 
        timeout=30)

        

    completed_stdout = f"Result of {file_path}:\n"
    if not completed_process.stderr and not completed_process.stdout: #Error check
        completed_stdout += f"No output produced\n"
    if completed_process.returncode != 0: #Error check
        completed_stdout += f"Process exited with code {completed_process.returncode}\n"
        
    completed_stdout += f"""
    STDOUT:{completed_process.stdout}
    
    STDERR:{completed_process.stderr}
    =============================================\n\n"""
    return completed_stdout





schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executing/running the content of a file located at the specified file path relative to the given working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to run, relative to the directory.",
                }
            },
            "required": ["file_path"],
        },
    },
}
