s1 = "kodnest"
s2 = "Kodnest"
if s1 == s2:
    print("strings are equal")
else:
    print("strings are not equal")
if id(s1) == id(s2):
    print("References are equal")
else:
    print("References are not equal")