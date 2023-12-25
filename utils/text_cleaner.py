import string

def text_cleaning(text):
    text = "".join([char for char in text if char not in string.punctuation])
    return text