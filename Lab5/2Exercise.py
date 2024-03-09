import re

def match_ab_strings(text):
  """
  This function checks if a string matches the pattern 'a' followed by two to three 'b's.

  Args:
      text: The string to be checked.

  Returns:
      True if the string matches the pattern, False otherwise.
  """
  pattern = r"ab{2,3}"
  return bool(re.match(pattern, text))

# Test cases
strings = ["ab", "abb", "abbb", "ac", "abbbb"]
for string in strings:
  if match_ab_strings(string):
    print(f"'{string}' matches the pattern")
  else:
    print(f"'{string}' does not match the pattern")
