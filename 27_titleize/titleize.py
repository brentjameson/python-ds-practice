def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return ' '.join([word.capitalize() for word in phrase.lower().split(' ')])

# sprinboard version -- built in method!

def titleize_sb(phrase):
    return phrase.title()
