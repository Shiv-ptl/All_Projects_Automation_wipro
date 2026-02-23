#fixture dependency - the second fixture will work when the first

import pytest

def test(fixture_b):
    assert fixture_b == "Data from A + Data from B"


#fixture_b automatically receives the values returned by fixture_a

#fixture_a
#fixture_b
#test


