#match - match the exact sequence

import  re
from re import match

#o/p match obj - matched sequence and span()  - start and end index

text = "Shivanshu Patel"
result = re.match("Shivanshu",text)

print(result)

#using pattern

test_str = "1234546243147abcasdfghjklabcABCqwertyuiop"
pattern = re.compile("abc")
#re.finditer() finds all non -overlapping matches of a pattern in a string and
#returns an iterator of match objects (not a list)

matches = pattern.finditer(test_str)

for match in matches:
    print(match)

#search operation searches the entire string
#returns only the first occurrence

text = "python is Powerful asd Powerful"
result = re.search("Powerful",text)
print(result)

#searches--- search entire string -used when we have to find the occurrences
#match --- beginning only -- validate the formats
#finditer()---Find all substrings where re match and returns them as iterator
#findall()--find all the substring where the re match and returns a list

#findall()

my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.finditer(my_string)

#group() -- returns the string matched by the RE
#start() -- returns the starting position of the match
#end() --returns the ending position of the match
#span() --returns a tuple containing the (start,end) position
for match in matches:
    print(match)
    print(match.span(),match.start(),match.end())
    print(match.group())#returns the substring that was matched by the RE

#special characters
#meta characters
#regular expressions

#patter meaning

#abc ,atches exact text
#[abc] a or b or c


#[0-9] digit

text = "I like abc and 12345ABCDEFGH"
result = re.findall("[0-9]",text)
print(result)

#'a b'
text = "cat bat rat mat"
result = re.findall("cat|bat",text)
print(result)

#any single char
text = "cat bat rat bob"
result = re.findall("c.t",text)
print(result)



'''
Special sequences begin with a backslash \.
Sequence    Meaning    Example
\d  Digit (0–9)    \d\d
\D  Non-digit  \D
\w  Word char (a-z, A-Z, 0-9, _)   \w+
\W  Non-word char  \W
\s  Whitespace \s
\S  Non-whitespace \S
\b  Word boundary  \bcat\b
\B  Not a word boundary    \Bcat
'''
#\d digit (0-9) \d\d
print(re.findall(r"\d","Order 123 costs 450"))
#\D Non Digit
print(re.findall(r"\D","Order 123 costs 450"))

#\w Word char (a-z,A-Z,0-9,_)
text = "Python_3 version!"
result = re.findall(r"\w",text)
print(result)

#\W Non-word char   \W
#matches anything that is NOT a word character.
text = "Hello@123!"
result  = re.findall(r"\W",text)
print(result)

#\s Whitespace spaces,tabs and newline
text = "Hello world\nPython"
result = re.findall(r"\s",text)
print(result)

#\b word boundary - matches position at start or end of a word
text = "cat scatter catalog"
result = re.findall(r"\bcat\b",text)
print(result)

#matches only full word "cat"

#\B Not a word boundry \Bcat - matches when pattern is NOT at word boundary
text = "cat scatter catalog"
result = re.findall(r"cat\B",text)
print(result)

"""
Meta - characters
have
special
meaning in regex.

Meta - character
Meaning
.Any
character
^ Start
of
string
$   End
of
string
*0 or more
+   1 or more
?   0 or 1
{n}
Exactly
n
times
{n, }
n or more
{n, m}
Between
n and m
[]
Character
set
()
Grouping
"""

#^ Start of string
text = "Python is easy Python"
print(re.findall(r"^Python",text))

#$ End on string
text = "Python is easy"
print(re.findall(r"easy$",text))

text = ["Python is easy","its easy","i am feeling good"]

for line in text:
    if re.findall(r"easy$", line):
        print(line)

#* 0 or more
text = "ab abb abbb a n"
print(re.findall(r"ab*",text))

#+ 1 or more
text = "ab abb abbb a n"
print(re.findall(r"ab+",text))

#? 0 re 1
text ="color colour colr"
print(re.findall(r"colou?r",text))

#{n} Exactly n times
text = "111 22 333 6877"
print(re.findall(r"\d{3}",text))

#{n,} n or more
text = "1 22 333 4444"
print(re.findall(r"\d{3,}",text))


#{n,m} between n and m
text = "1 22 333 4444"
print(re.findall(r"\d{2,3}",text))


#[] character set
text = "apple banana cat"
print(re.findall(r"[abc]",text))

#() Grouping
text = "2026-02-11"
result = re.findall(r"(\d{4})-(\d{2})-(\d{2})",text)
print(result)

