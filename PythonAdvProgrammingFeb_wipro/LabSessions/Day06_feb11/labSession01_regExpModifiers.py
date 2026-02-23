# Regular expression modifier
#
import re

from PythonPragramming.Matchsear import pattern

# Write a regex to check if a string contains only digits.
text = "1234Abcd"
print(bool(re.fullmatch(r"\d+",text)))

# Write a pattern to match a 10-digit mobile number.
text = "Call me at 9876543210 or 9123456789"#"9005115507 asf 12345345"
print(re.findall(r"\d{10}",text))


# Find all lowercase letters in a string.
print(re.findall(r"[a-z]","My name is Shivanshu Patel."))
# Extract all uppercase letters from a sentence.

print(re.findall(r"[A-Z]","My name is Shivanshu Patel."))
# Match a string that starts with "Hello".
text = "Hello world"
print(bool(re.search(r"^Hello", text)))

# Match a string that ends with "world".
text = "Hello world"
print(bool(re.search(r"world$", text)))
# Find all words separated by spaces.
text = "Python is very easy"
print(re.findall(r"\w+", text))

# Match exactly 5 characters.
text = "Patel"
print(bool(re.fullmatch(r".{5}", text)))

# Find all occurrences of the word "python" (case-sensitive).
text = "I am learning python. Python is a programming language.I will use python in testing"
print(re.findall(r"python",text))
# Replace all spaces in a string with underscores.
text = "I am learning python.\tPython is a programming language.\nI will use python in testing"
print(re.sub(r"\s","_",text))

# Find all occurrences of the word "python" (not case-sensitive).
text = "I am learning python. Python is a programming language.I will use python in testing"
print(re.findall(r"python",text,re.IGNORECASE))

'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''

#re.MULTILINE re.M  ^and$ match each line
text = "hello\npython"
print(re.findall("^python",text,re.M))

#re.DOTALL re.s   . matches newline
text = "Hello\nWorld"
print(re.search("Hello.*World",text,re.S))

#re.VERBOSE re.X write readable regex with comments- make it more readable
import re
pattern =re.compile(r"""34543ffddf..%!@#$%^44""",re.X)
print(pattern)

#re.ASCII re.A ASCII-only matching
print(re.findall(r"\w+",text,re.A))

#re.DEBUG -debu pattern
pattern = re.compile(r"""234fds%...^^&24""",re.DEBUG)
print(pattern)

#assertions--validating the output or checking certain conditions
"""
# ^ → Start of string
# $ → End of string
# \b → Word boundary
# \B → Not word boundary
# (?=...) → Positive Lookahead
# (?!...) → Negative Lookahead
# (?<=...) → Positive Lookbehind
# (?<!...) → Negative Lookbehind
"""

import re

text ="Python is easy"
print(re.findall (r"^Python", text))


text = "Python is easy"
print(re.findall( r"easy$", text))


text = "cat scatter catalog"
print(re.findall( r"\bcat\b", text))


text = "cat scatter catalog"
print(re.findall(  r"cat\B", text))

#Positive Lookahead= watch only if followed by somethi

text = "user1 admin2 test"

print(re.findall( r"\w+(?=\d)", text))

#Negative Locleanear

Text = "user1 admin test2"
#(?=...) ->positive lookahead = matches only if followed by something
text = "user admin2 test"
print(re.findall(r"\w+(?=\d)",text))

#(?!...) ->negative lookahead

text = "user1 admin test1"
print(re.findall(r"\w+(?!\d)",text))

#(?<=...) positive lookback match only if preceeded by something
test = "Price 500"
print(re.findall(r"\w+(?<=)\d",text))

#(?<!...) negative lookback
test = "300 500"
print(re.findall(r"\w+(?<!)\d+",text))


#MCQ's
# What is the output?
# import re
#
# print(re.findall(r"\d*", "ab12cd3"))
#
# A) ['12', '3']
# B) ['', '', '12', '', '3', '']
# C) ['', '', '12', '', '', '3', '']
# D) ['12', '', '3']
#C

# What does this return?
# re.findall(r"^ab", "ab\nabc\nab", re.M)
#
# A) ['ab']
# B) ['ab', 'ab']
# C) ['ab', 'abc', 'ab']
# D) []
#C

# What is the output?
# re.findall(r"[A-Z]+", "PyTHon IS Fun")
#
# A) ['P', 'TH', 'IS', 'F']
# B) ['TH', 'IS', 'F']
# C) ['P', 'TH', 'IS', 'F', 'F']
# D) ['P', 'T', 'H', 'I', 'S', 'F'
#A

# What will this print?
# re.findall(r"(ha){2,3}", "hahaha haha hahahaha")
#
# A) ['hahaha', 'haha', 'hahaha']
# B) ['ha', 'ha', 'ha']
# C) ['ha', 'ha']
# D) ['ha', 'ha', 'ha', 'ha']
#B

# What is the output?
# re.findall(r"\b\w{4}\b", "This test code runs well")
#
# A) ['This', 'test', 'code', 'runs', 'well']
# B) ['This', 'test', 'code', 'runs']
# C) ['This', 'code', 'runs']
# D) ['well']
#A

# What happens here?
# re.findall(r".+?", "abc")
#
# A) ['abc']
# B) ['a', 'b', 'c']
# C) ['a', 'bc']
# D) ['abc', '']
#B

# (Hint: Non - greedy quantifier)
#
# What is the output?
# re.findall(r"\w+\B", "cat scatter dog")
#
# A) ['cat', 'scatter', 'dog']
# B) ['sca', 'scatte']
# C) ['sca', 'scatte', 'do']
# D) ['scatte']
#
# What will this return?
# re.findall(r"(ab|cd)+", "ab cd abab cdcd")
#
# A) ['ab', 'cd', 'abab', 'cdcd']
# B) ['ab', 'cd', 'ab', 'cd']
# C) ['ab', 'cd', 'ab', 'ab', 'cd', 'cd']
# D) ['abab', 'cdcd']
#B

# What is the result?
# re.findall(r"\Acat", "cat\ncat")
#
# A) ['cat']
# B) ['cat', 'cat']
# C) []
# D) Error
#A

# (Hint: \A vs ^)
#
# What happens here?
# re.findall(r"(?<!\d)\d{2}", "123 45 6 789")
#
# A) ['12', '45', '78']
# B) ['23', '45', '89']
# C) ['45', '78']
# D) ['23', '45']
#A

#re.ASCII re.A ASCII-only matching
text = "café résumé naïve"#"What does this return?"
print(re.findall(r"\w+",text,re.A))