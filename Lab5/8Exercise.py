import re
def split_at_uppercase(text):
  
  return re.findall(r'[A-Z][a-z]*|\b[a-z]+\b', text)


text = "ThisIsAStringWithMixedCase"
split_words = split_at_uppercase(text)

print("Original string:", text)
print("Split words:", split_words)
