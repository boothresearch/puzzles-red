def count_letters(word):
    all_freq = {}
    for i in word:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def find_anagrams(word, candidates):
    word = word.lower()
    hist = count_letters(word)
    anagrams = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower!=word:
            if count_letters(candidate_lower)==hist:
                anagrams.append(candidate)
    return anagrams
