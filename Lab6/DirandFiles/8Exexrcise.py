import os

def delete_file(path):
  
  if not os.path.exists(path):
    print(f"Error: File does not exist - {path}")
    return

  
  if not os.path.isfile(path):
    print(f"Error: Path points to a directory, not a file - {path}")
    return

  
  if not os.access(path, os.W_OK):
    print(f"Error: Insufficient permissions to delete the file - {path}")
    return

  
  try:
    os.remove(path)
    print(f"File deleted successfully: {path}")
  except OSError as e:
    print(f"Error deleting file: {path} - {e}")


path = input("Enter the path of the file to delete: ")


delete_file(path)
