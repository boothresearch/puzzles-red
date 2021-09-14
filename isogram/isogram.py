def count_letters_alpha(word):
    all_freq = {}
    for i in word:
        if i.isalpha():
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    return all_freq

def is_isogram(string):
    alpha_freq = count_letters_alpha(string.lower())
    try:
        if max(alpha_freq.values())==1:
            return True
    except ValueError:
        return True
    return False
