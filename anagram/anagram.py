def find_anagrams(word, candidates):
    word = word.lower()
    hist = dict(enumerate(word))
    anagrams = []
    for candidate in candidates:
        candidate = candidate.lower()
        if dict(enumerate(candidate))==hist:
            anagrams.append(candidate)
    return anagrams
