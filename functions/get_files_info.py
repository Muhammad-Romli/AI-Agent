import os

def get_files_info(working_directory:str, directory:str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        #Below, will compare the commonpath to the working_dir_abs itself and return True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        #String below, is a placeholder
        dir_name =  "current" if directory == "." else f"'{directory}'"
        return_str = f"Result for {dir_name} directory:"

        
        if not valid_target_dir:
            return return_str + f'\n    Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        if not os.path.isdir(target_dir):
            return return_str + f'\n    Error: "{directory}" is not a directory'

        for file in os.listdir(target_dir):
            name = file
            full_filepath = os.path.join(target_dir, file)
            file_size =os.path.getsize(full_filepath)
            is_dir = os.path.isdir(full_filepath)

            return_str += f"\n-{name}: file_size={file_size} bytes, is_dir={is_dir}"
        return return_str

    except Exception as e:
        return f"Error: get_files_info is returning error: {e}"
