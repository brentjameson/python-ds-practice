def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flip = ''
    for char in phrase:
        if char.islower():
            # a
            if char == to_swap:
                # a = a
                flip += char.upper()
                # a --> A
            elif char.upper() == to_swap:
                flip += char.upper()
            else:
                flip += char
        if char.isupper():
            # A
            if char == to_swap:
                # A = A
                flip += char.lower()
                # a --> A
            elif char.lower() == to_swap:
                flip += char.lower()
            else:
                flip += char
    return flip

# Springboard solution below
# >>> flip_case('Aaaahhh', 'A')
        # 'AaaaHHH'

def flip_case_sb(phrase, to_swap):
    to_swap = to_swap.lower()
    # to_swap: A --> a 
    out = ''

    for ltr in phrase:
        if ltr.lower() == to_swap:
            # ltr: A, ltr.lower: a == a
            ltr = ltr.swapcase()
            # ltr A --> a
        out += ltr
            # A --> a
            # a --> A
    return out

