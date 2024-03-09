import os

def check_path_access(path):
  
  if not os.path.exists(path):
    print(f"Path does not exist: {path}")
    return

  
  if not os.access(path, os.R_OK):
    print(f"Path is not readable: {path}")
  else:
    print(f"Path is readable: {path}")

  
  try:
    with open(os.path.join(path, "tmp.txt"), "w") as f:
      f.write("Test")
    os.remove(os.path.join(path, "tmp.txt"))
    print(f"Path is writable: {path}")
  except OSError:
    print(f"Path is not writable: {path}")

 
  if os.path.isfile(path):
    if not os.access(path, os.X_OK):
      print(f"Path is not executable: {path}")
    else:
      print(f"Path is executable: {path}")
  else:
    print(f"Executability check not applicable for directories: {path}")


path = input("Enter the path to check access: ")


check_path_access(path)
