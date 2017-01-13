# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    # implement your solution here
    
    # 1) Split up 'text' into words with .split()
    # 2) iterate through words, and look for each word in the each language
    # 3) count the number of matches in each language
    # 4) return the language with highest matches
    
    text = text.split()
    
    lang_count = {}
    
    for lang in languages:
        counter = 0
        for word in text:
            if word in lang['common_words']:
                counter += 1
        lang_count[lang['name']] = counter
        print(lang['name'] + ' : ' + str(counter))
    
    
    # Set starting value for finding max
    lang_max_count = 0
    lang_max_name = ''
    
    # Get dict key and val for highest key value
    for lang in lang_count:
        if lang_max_count < lang_count[lang]:
            lang_max_count = lang_count[lang]
            lang_max_name = lang
    
    return lang_max_name

