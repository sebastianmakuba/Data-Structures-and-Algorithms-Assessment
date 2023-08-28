import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator).lower()

    # Tokenize the sentence into words
    words = sentence.split()

    # Count word frequency using a dictionary
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Test case
sentence = " is a test. This is only a test."
result = word_frequency(sentence)
print(result) 
