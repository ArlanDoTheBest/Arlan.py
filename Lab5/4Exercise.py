import re

def find_uppercase_lowercase(text):
 
  pattern = r"[A-Z][a-z]+"  
  return re.findall(pattern, text)


text = "ThisIsAStringWithMixedCase But_also_lowercase_words"
sequences = find_uppercase_lowercase(text)

if sequences:
  print("Found sequences of uppercase followed by lowercase:", sequences)
else:
  print("No sequences of uppercase followed by lowercase found in the text.")
