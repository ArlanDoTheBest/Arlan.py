import os

def check_path(path):
  
  
  if os.path.exists(path):
    
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(f"Path exists: {path}")
    print(f"\tFilename: {filename}")
    print(f"\tDirectory: {directory}")
  else:
    print(f"Path does not exist: {path}")


path = input("Enter the path to check: ")


check_path(path)
