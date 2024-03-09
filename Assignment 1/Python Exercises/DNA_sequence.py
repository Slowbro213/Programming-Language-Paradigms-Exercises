def findRepeatedDnaSequences(Sequence):
    seen = set()
    list = set()
    for i in range(len(Sequence)):
        SubSequence = Sequence[i:i+10]
        if SubSequence not in seen:
            seen.add(SubSequence)
        else:
            list.add(SubSequence)


    return list


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))
s = "AAAAAAAAAAAAA"
print(findRepeatedDnaSequences(s))