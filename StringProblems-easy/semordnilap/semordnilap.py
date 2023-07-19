def semordnilap(words):
    pairs=[]
    wordSet=set(words)
    for word in words:
        rev=word[::-1]
        if rev in wordSet and rev!=word:
            pairs.append([word,rev])
            wordSet.remove(word)
            wordSet.remove(rev)
    # Write your code here.
    return pairs
