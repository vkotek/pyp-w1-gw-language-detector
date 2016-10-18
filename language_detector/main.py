# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    result = None
    result_counter = 0
    for lang_doc in languages:
        counter = len([w for w in lang_doc['common_words'] if w in text])
        if counter > result_counter:
            result_counter = counter
            result = lang_doc['name']
    return result
