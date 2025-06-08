s1 = "KODNEST"
s2 = "kodnest"
s1 = s1.lower()
if s1 == s2:
    print("strings are equal")
else:
    print("strings are mot equal")
if id(s1) == id(s2):
    print("References are equal")
else:
    print("References are not equal")