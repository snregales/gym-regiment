#! /usr/bin/env python

"""
example.py
"""

def name(first: str, last: str = None) -> str:
    """Given first and last name inject them into a sentence string
    Arguments:
        first {str} -- first name
    Keyword Arguments:
        last {str} -- last name (default: {None})
    Returns:
        str -- a new compound string with first and last name injected
    """
    return f"Hello, I'm {f'{first} {last}' if last else first}"

if __name__ == '__main__':
    print(name("Sharlon", "Regales"))
