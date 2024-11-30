import os
import shutil

def delete_specified_folder(root_directory, folder_to_delete):
    try:
        # Walk through the directory tree under the root directory
        for root, dirs, files in os.walk(root_directory):
            if folder_to_delete in dirs:
                # Full path to the folder to delete
                folder_path = os.path.join(root, folder_to_delete)
                
                try:
                    shutil.rmtree(folder_path)
                    print(f"Deleted folder: {folder_path}")
                except Exception as e:
                    print(f"Failed to delete {folder_path}: {e}")
            else:
                print(f"Folder '{folder_to_delete}' not found in '{root}'")
    
    except FileNotFoundError:
        print("Root directory not found")
    except PermissionError:
        print("Permission denied")

# Example usage:
root_directory = "/home/clbaker/cse220/lab3/Scarab-infra/cse220/exp"  # Starting point of the folder structure
folder_to_delete = input("File to remove: ")  # Replace with the actual folder name you want to delete
delete_specified_folder(root_directory, folder_to_delete)

# if isinstance(csv_files, dict):
#     for folder, files in csv_files.items():
#         print(f"CSV files in {folder}:")
#         for file in files:
#             print(f" - {file}")
# else:
#     print(csv_files)