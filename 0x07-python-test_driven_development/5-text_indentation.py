#!/usr/bin/python3

"""
Indentation function
"""


def text_indentation(text):
    """
    Prints a new line after '.', '?', ':' characters

    Arguments:
        text - str

    Raises:
        TypeError - if text is not str

    Return:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    sentence = ""
    startline = 1
    for char in text:
        if char in ".?:":
            sentence += char + "\n\n"
            startline = 1
        else:
            if startline and (char in " \n\t\r"):
                continue
            sentence += char
            startline = 0
        new_text += sentence
        sentence = ""
    print(new_text)
