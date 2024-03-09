def Longest_substring_with_dis1nct_characters(string):
    substring = ""
    maxsubstring = ""

    for i in range(len(string)):
        if s[i] not in substring:
            substring += s[i]
        else:
            if len(substring) > len(maxsubstring):
                maxsubstring = substring
            substring += s[i]
            start_index = substring.find(s[i])
            substring = substring[start_index + 1:]

    return len(substring) if len(substring) > len(maxsubstring) else len(maxsubstring)



s = "abcabcbb"
print( "Longest substring for " + s + " is: " + str(Longest_substring_with_dis1nct_characters(s)))
s = "bbbbbb"
print( "Longest substring for " + s + " is: " + str(Longest_substring_with_dis1nct_characters(s)))
s = "pwwkew"
print( "Longest substring for " + s + " is: " + str(Longest_substring_with_dis1nct_characters(s)))
s = "abcdeabcdefabcdefg"
print( "Longest substring for " + s + " is: " + str(Longest_substring_with_dis1nct_characters(s)))
