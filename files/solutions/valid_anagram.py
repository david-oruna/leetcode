#simple solutin
def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


# hash table 

def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
