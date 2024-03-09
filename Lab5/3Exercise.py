import re

def find_lowercase_sequences(text):
  
  pattern = r"[a-z]+_[a-z]+"  
  return re.findall(pattern, text)


text = "This_is_a_string_with_lowercase_sequences_and_More_examples"
sequences = find_lowercase_sequences(text)

if sequences:
  print("Found lowercase sequences:", sequences)
else:
  print("No lowercase sequences found in the text.")