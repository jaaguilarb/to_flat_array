
flat = []

def review(x):
    """Unpack a nested array or put the integer element in flat array.

    Keyword arguments:
    x -- the element, can be an integer or an nested array

    """
    global flat
    if  isinstance(x,int):
        flat.append(x)
    else:
        map(review,x)
    return flat

def to_flat(na):
    """Convert to flat array.

    Keyword arguments:
    na -- the nested arrays of integers

    """
    print na
    fa = map(review,na)
    return flat
