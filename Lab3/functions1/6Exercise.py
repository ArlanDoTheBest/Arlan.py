def reversesentence():
    sentence = str(input())
    reversed_sentence = " ".join(reversed(sentence.split()))
    print(reversed_sentence)

reversesentence()