# oxford_comma.py

def oxford_comma(items):
    '''Return a string with proper Oxford comma formatting.'''
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        # Join all elements with commas, except the last one, which is joined with "and"
        return f"{', '.join(items[:-1])}, and {items[-1]}"
