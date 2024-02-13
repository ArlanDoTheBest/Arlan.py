def checkforpalindrome(str):
    if(str == str[::-1]):
        print("The word is palindrome")
    else:
        print("The word is not palindrome")
        
str = str(input())
checkforpalindrome(str)