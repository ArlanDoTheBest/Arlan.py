import re

def replace_separators(text):
 
  pattern = r"\s|\,|\."  
  return re.sub(pattern, ":", text)


text = "This is a string, with spaces. commas, and dots."
modified_text = replace_separators(text)

print("Original text:", text)
print("Text with separators replaced by colons:", modified_text)
