# Strings are immutable in Python
# del str[1]  - Will not work

print("=============== String split() ===============")
# Syntax
# str.split(sep=None, maxsplit=-1)
#       sep
#			If sep is not specified or is None, a different splitting algorithm
# 			is applied: runs of consecutive whitespace are regarded as a single separato
# 		maxsplit 
# 			If maxsplit is given, the list will have at most maxsplit + 1 elements
#			result will contain no empty strings at the start or end if the string has leading or trailing whitespace

# Splitting an empty string or a string consisting of just whitespace with a None separator returns []
print('"     ".split(): ', "     ".split())
print('" 1   2   3   ".split() [whitespaces will be trimmed]: ', "   1   2   3   ".split())
print('"a1 a2 a3".split(): [without seperator] ', "a1 a2 a3".split())

print("'1 2 3'.split(maxsplit=1): ", '1 2 3'.split(maxsplit=1))
# OR
print("'1 2 3'.split(" ",1): ", '1 2 3'.split(" ",1))


print("\n================ str.splitlines() ================")
# Syntax :
# str.splitlines([keepends])

print('"ab c\n\nde fg\tkl\t\n".splitlines(): ', "ab c\n\nde fg\tkl\t\n".splitlines())
print('"ab c\n\nde fg\tkl\t\n".splitlines(keepends = True): ', "ab c\n\nde fg\tkl\t\n".splitlines(keepends = True))


print("\n========= String Concatenation (Most Memory Efficenct) =========")
k = "".join([num for num in ["fdsg ","asfsdf "]])
print('"".join([num for num in ["fdsg ","asfsdf "]]): ', k)

print("\n========= str.casefold() - IngnoreEqualCase =========")
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
print('"python".casefold() == "PythoN".casefold(): ', "python".casefold() == "PythoN".casefold())


print("\n================ String Operations ================")
print('"str with 4 words".capitalize() [first character capitalized]: ', "str with 4 words".capitalize(),"\n")

# Strip
test_txt = "test"
strip_txt = test_txt + "    |whitespaces from both sides will be removed|   ".strip() + test_txt
print('"     whitespaces from both sides will be removed    ".strip() => ', strip_txt)

lstrip_txt = test_txt + "    |left whitespaces will be removed|        ".lstrip() + test_txt
print('"     left whitespaces will be removed    ".lstrip()  => ', lstrip_txt)

rstrip_txt = test_txt +"      |right whitespaces will be removed|       ".rstrip() + test_txt
print('"     right whitespaces will be removed    ".rstrip()  => ', rstrip_txt)

print("\n=============== Enumerate String ===============")
str = "Python"
for idx, ch in enumerate(str):
	print("index is %d and character is %s" % (idx, ch))



