import random
import data

def bb3name():
    return 'The ' + data.adjectives[random.randint(0, len(data.adjectives) - 1)] + ' ' + data.nouns[random.randint(0, len(data.nouns) - 1)] + ' of ' + data.nouns[random.randint(0, len(data.nouns) - 1)] + 's'