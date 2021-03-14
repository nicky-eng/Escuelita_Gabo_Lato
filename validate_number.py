def validate_number(value):
    "If value is an integer it returns that value, if it is not, it raises a TypeError."
    if not isinstance(value, (int, float, complex)):
        raise TypeError("{} is not a number".format(value))
    return value