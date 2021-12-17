def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
# I misinterpreted and capitalized the first letter of each word
    phrase_list = phrase.split()
    out = []
    for word in phrase_list:
       out.append(word.capitalize())
    return ' '.join(out)

def capitalize_sb(phrase):
    return phrase.capitalize()
