str1 = "madam".lower()
str2 = "Madam".lower()
if str1 == str2[::-1]:
    print("Strings are palindrome")
else:
    print("Strings are not Palindrome")