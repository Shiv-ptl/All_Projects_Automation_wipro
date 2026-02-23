# Python File Handling MCQs (CSV, XML, JSON)

# ---------------- CSV Handling ----------------

# 1. What is the default delimiter used by Python’s csv.reader?
# A. |
# B. \t
# C. ,
# D. ;
#C

# 2. Which mode is mandatory while opening a CSV file on Windows to avoid blank lines?
# A. "r"
# B. "rb"
# C. "r", newline=""
# D. "rt"
#C

# 3. What does csv.DictReader return for each row?
# A. List
# B. Tuple
# C. Dictionary
# D. Set
#C

# 4. If a CSV file has more columns than fieldnames passed to DictReader, what happens?
# A. Extra columns are ignored
# B. Raises ValueError
# C. Extra values are stored under key None
# D. File is not read
#C

# 5. Which parameter is used to change the delimiter in csv.reader?
# A. separator
# B. split
# C. delimiter
# D. sep
#C

# 6. Which object is returned by csv.writer()?
# A. File object
# B. Iterator
# C. Writer object with writerow() method
# D. Dictionary
#C

# 7. What happens if writerow() receives a dictionary?
# A. Values are written automatically
# B. Keys are written
# C. Raises TypeError
# D. Writes only values in random order
#C

# ---------------- XML Handling ----------------

# 8. Which module is most commonly used for basic XML parsing in Python?
# A. xml.dom
# B. lxml
# C. xml.etree.ElementTree
# D. BeautifulSoup
#C

# 9. What does ElementTree.parse() return?
# A. Root element
# B. XML string
# C. ElementTree object
# D. List of elements
#C

# 10. Which method returns the root element of an XML document?
# A. getRoot()
# B. root()
# C. getroot()
# D. findroot()
#C

# 11. What is the output type of element.text?
# A. List
# B. String
# C. XML object
# D. Dictionary
#B

# 12. If an XML tag is self-closing, what is element.text?
# A. Empty string
# B. None
# C. Raises error
# D. " "
#B

# 13. Which method finds only the first matching child?
# A. findall()
# B. find()
# C. iter()
# D. getchildren()
#B

# 14. How are attributes of an XML element accessed?
# A. element.attribute
# B. element.attrib
# C. element.getAttribute()
# D. element.attrs()
#B

# ---------------- JSON Handling ----------------

# 15. Which Python type does a JSON object map to?
# A. List
# B. Tuple
# C. Dictionary
# D. Set
#C

# 16. What is the difference between json.load() and json.loads()?
# A. Both are same
# B. load() reads string, loads() reads file
# C. load() reads file, loads() reads string
# D. Both read only files
#C

# 17. Which of the following is NOT JSON serializable by default?
# A. List
# B. Dictionary
# C. Tuple
# D. Set
#D

# 18. What will json.dumps() return?
# A. Python dictionary
# B. JSON file
# C. JSON string
# D. Byte object
#C

# 19. Which parameter makes JSON output human-readable?
# A. sort_keys
# B. indent
# C. pretty
# D. spacing
#B

# 20. If a JSON key is duplicated, what happens during parsing?
# A. Raises error
# B. Both values stored
# C. Last value overwrites previous
# D. First value retained
#C