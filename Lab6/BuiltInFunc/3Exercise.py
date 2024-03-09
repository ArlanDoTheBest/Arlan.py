def is_palindrome(text):
 

  
  text = ''.join(char.lower() for char in text if char.isalnum())
  return text == text[::-1]


text1 = "Racecar"
text2 = "Hello, world!"

print(f"{text1} is a palindrome: {is_palindrome(text1)}")
print(f"{text2} is a palindrome: {is_palindrome(text2)}")