import re, string
import nltk

regex = re.compile('[%s]' % re.escape(string.punctuation))

def clean_string(string):
    filtered = []
    tokens = nltk.word_tokenize(string.lower())
    for token in tokens:
        token = regex.sub('',token)
        if not token == '':
            filtered.append(token)
    return filtered

'''
#test the code
with open('story.txt', 'rb') as f:
    for line in f.readlines():
        print clean_string(line)
        raw_input()
'''

