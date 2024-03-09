import shutil

def copy_file(source_file, destination_file):
  
  try:
    shutil.copyfile(source_file, destination_file)
    print(f"File copied successfully: {source_file} -> {destination_file}")
  except FileNotFoundError:
    print(f"Error: Source file not found - {source_file}")
  except PermissionError:
    print(f"Error: Insufficient permissions to copy the file.")


source_file = input("Enter the source file to copy: ")
destination_file = input("Enter the destination filename: ")


copy_file(source_file, destination_file)
