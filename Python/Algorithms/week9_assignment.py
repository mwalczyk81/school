def naive_string_matching(text, pattern):
    """
    Implement the naive string matching algorithm.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    indices = []
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            indices.append(i)
    
    return indices

def rabin_karp(text, pattern, d, q):
    """
    Implement the Rabin-Karp string matching algorithm.
    'd' is the number of characters in the input alphabet, and 'q' is a prime number.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    indices = []
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    
    p = 0
    t = 0
    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for s in range(n - m + 1):
        if p == t:
            if pattern == text[s:s+m]:
                indices.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    
    return indices

def kmp_pattern_preprocessing(pattern):
    """
    Preprocess the pattern for the KMP string matching algorithm.
    Return the lps (longest proper prefix which is also a suffix) array.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def trie_insert(root, key):
    """
    Insert 'key' into the trie rooted at 'root'.
    """
    if isinstance(root, dict):
        node = root
        for char in key:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['end_of_word'] = True
    elif isinstance(root, list):
        node = root
        for char in key:
            found = False
            for child in node:
                if child[0] == char:
                    node = child[1]
                    found = True
                    break
            if not found:
                new_node = [char, []]
                node.append(new_node)
                node = new_node[1]
        node.append(None)