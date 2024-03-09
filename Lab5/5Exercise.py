import re

def match_aab_strings(text):
  
  pattern = r"a.*b"  
  return bool(re.match(pattern, text))


strings = ["ab", "aab", "abbcd", "ac", "b"]
for string in strings:
  if match_aab_strings(string):
    print(f"'{string}' matches the pattern")
  else:
    print(f"'{string}' does not match the pattern")
