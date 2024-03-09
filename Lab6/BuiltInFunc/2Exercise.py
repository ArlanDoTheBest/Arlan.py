def count_uppercase_lowercase(text):
  

  counts = {
    'uppercase': sum(char.isupper() for char in text),
    'lowercase': sum(char.islower() for char in text)
  }
  return counts


text = "This is a String With MiXeD CaSe."
letter_counts = count_uppercase_lowercase(text)
print("Uppercase letters:", letter_counts['uppercase'])
print("Lowercase letters:", letter_counts['lowercase'])