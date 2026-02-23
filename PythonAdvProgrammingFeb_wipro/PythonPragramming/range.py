#range does not create a list ,it creats object (memory efficient)
a = range(5)
print(a[1])

a=range(15,2,-1)
for i in a:
    print(i)


# usage:
# fast interation
# loops and indexing
# counters are clear to understnd



prices= [ 100,200,300,400]
for i in range(len(prices)):
    if i%2==0:
        print("discount applied on item ",i)

import  time

for second in range(10):
    print("Checking the status at second - ",second)
    time.sleep(1)


# 1. Which of the following is true about range() in Python 2?
# A. It returns a generator
# B. It returns a list
# C. It returns a tuple
# D. It returns an iterator

#B

# 2. Which function was introduced to reduce memory usage in Python 2?
# A. range()
# B. list()
# C. enumerate()
# D. xrange()

#D


# 3. What is the output type of xrange(1, 5) in Python 2?
# A. List
# B. Tuple
# C. xrange object
# D. Generator

#C

# 4. Which of the following statements is correct?
# A. xrange exists in Python 3
# B. range is removed in Python 3
# C. xrange is removed in Python 3
# D. Both range and xrange exist in Python 3
#C

# 5. Which of the following consumes more memory in Python 2?
# A. xrange(1, 1000000)
# B. range(1, 1000000)
# C. Both consume equal memory
# D. Neither consumes memory
#B

# 6. Which function supports slicing in Python 2?
# A. range()
# B. xrange()
# C. Both
# D. Neither
#A

# 7. What happens when you try to use xrange() in Python 3?
# A. It works normally
# B. It gives a warning
# C. It raises NameError
# D. It returns None
#C

# 8. Which of the following is TRUE about range() in Python 3?
# A. It returns a list
# B. It behaves like Python 2 xrange
# C. It loads all values into memory
# D. It is slower than Python 2 range
#B


# 9. Which function is more suitable for looping over very large numbers in Python 2?
# A. range()
# B. list()
# C. tuple()
# D. xrange()
#D

# 10. Which of the following statements about xrange is FALSE?
# A. It is memory efficient
# B. It supports indexing
# C. It supports slicing
# D. It generates values lazily
#C

# 11. In Python 3, which function should be used instead of xrange?
# A. list()
# B. tuple()
# C. iter()
# D. range()
#D

# 12. Which of the following code snippets creates a list in Python 2?
# A. xrange(1, 5)
# B. range(1, 5)
# C. iter(1, 5)
# D. enumerate(1, 5)
#B

# 13. What is the default starting value of range()?
# A. 1
# B. -1
# C. 0
# D. None
#C

# 14. Which version of Python first removed xrange()?
# A. Python 2.6
# B. Python 2.7
# C. Python 3.0
# D. Python 3.6
#C

# 15. Which of the following best describes range() in Python 3?
# A. List-based sequence
# B. Generator function
# C. Lazy iterable object
# D. Dictionary-like object
#C