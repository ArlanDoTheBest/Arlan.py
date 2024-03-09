def count_lines_readlines(filename):
  
  try:
    with open(filename, 'r') as f:
      lines = f.readlines()
      return len(lines)
  except FileNotFoundError:
    print(f"Error: File not found - {filename}")
    return 0


filename = input("Enter the filename: ")


number_of_lines = count_lines_readlines(filename)

if number_of_lines > 0:
  print(f"The file {filename} has {number_of_lines} lines.")
