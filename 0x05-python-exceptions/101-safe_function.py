#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        output = fct(*args)
    except Exception as a:
        sys.stderr.write("Exception: {}\n".format(a))
        output = None

    return (output)
