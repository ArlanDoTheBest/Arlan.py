import re
def camel_to_snake(text):
  
  
  pattern = r"(?<!^)([A-Z])"
  
  return re.sub(pattern, r"_\1", text).lower()


camel_case_text = "ThisIsACamelCaseString"
snake_case_text = camel_to_snake(camel_case_text)

print("Camel case:", camel_case_text)
print("Snake case:", snake_case_text)
