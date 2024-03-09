import string


alphabet = string.ascii_uppercase

for letter in alphabet:
  
  filename = letter + ".txt"
  
  
  with open(filename, "w") as f:
    
    f.write(letter)

print("Generated 26 text files (A.txt to Z.txt)")
