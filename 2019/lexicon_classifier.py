import emoji
import string


def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])

    return clean_text

def lexicon_classifier(line, trend):
    line = give_emoji_free_text(line)
    line = line.replace(trend, '')
    line = line.replace('  ', ' ')

    line = line.strip()

    if (len(line) == 0):
        return False

    if (line[0].isupper()):
        return False

    invalidChars = set(string.punctuation.replace("(", "…").replace(")", "...").replace('.', ".").replace('.', '.'))
    invalidChars = invalidChars.union(set(["%d" % i for i in range(0,10)])) # added numbers

    if any(char in invalidChars for char in line):
        return False

    tokens = line.split(' ')
    if (len(tokens) > 10 or len(tokens) < 3):
        return False



    return True