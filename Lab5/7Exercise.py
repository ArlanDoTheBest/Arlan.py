def snake_to_camel(text):
  
 
  words = text.split("_")
  
  camel_case = words[0] + "".join(word.capitalize() for word in words[1:])
  return camel_case


snake_case_text = "snake_case_string"
camel_case_text = snake_to_camel(snake_case_text)

print("Snake case:", snake_case_text)
print("Camel case:", camel_case_text)
