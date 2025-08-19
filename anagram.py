class anagram:
    def prog_anagram(a,b):
        if len(a)!=len(b):
            return False
        return sorted(a)==sorted(b)
print(anagram.prog_anagram("sai","sai"))
print(anagram.prog_anagram("sai","mohan"))
print(anagram.prog_anagram("",""))