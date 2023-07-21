def groupAnagrams(words):
    anagram_dictionary={}
    anagram_groups=[]
    for i in words:
        sorted_word=''.join(sorted(i))
        if sorted_word not in anagram_dictionary:
            anagram_dictionary[sorted_word]=[]

        anagram_dictionary[sorted_word].append(i)
 
    return list(anagram_dictionary.values())
    # Write your code here.
    
