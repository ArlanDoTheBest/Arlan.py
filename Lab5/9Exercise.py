import re
def insert_spaces(text):
 
  return re.sub(r"(?<!^)([A-Z])", r" \1", text)


text = "ThisIsAStringWithMixedCaseWords"
text_with_spaces = insert_spaces(text)

print("Original text:", text)
print("Text with spaces inserted:", text_with_spaces)
