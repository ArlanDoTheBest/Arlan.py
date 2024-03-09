def write_list_to_file_loop(data, filename):
  
  try:
    with open(filename, 'w') as f:
      for item in data:
        f.write(f"{item}\n")
  except FileNotFoundError:
    print(f"Error: Could not create file - {filename}")


data = ["item1", "item2", "item3"]
filename = "my_list.txt"


write_list_to_file_loop(data, filename)

print(f"List written to file: {filename}")
