import re

def match_ab_strings(text):
  
  pattern = r"ab*"
  return bool(re.match(pattern, text))

# Test cases
strings = ["ab", "abb", "abbb", "ac", "cba"]
for string in strings:
  if match_ab_strings(string):
    print(f"'{string}' matches the pattern")
  else:
    print(f"'{string}' does not match the pattern")
