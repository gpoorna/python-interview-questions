string1 = "Listen"
string2 = "silent"
string1 = list(string1.upper()) #strings are imutable in nature, so coverts them in list makes easy to manipulate the strings
string2 = list(string2.upper())
string2.sort(), string1.sort()
if string1 == string2:
    print("String are equal", "Anagram")
else:
    print("Not an Anagram")