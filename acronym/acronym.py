def abbreviate(words):
    acronym = '' 
    for s in words.split(' '):
        acronym += s[0] 
    return acronym
