from lib.verify_age import *
import pytest
"""
Given age under 15
It returns "Age shows 15, access dinied"
"""
def test_under_age():
    actual = verify_age("2009-2-1") 
    expected = "Age shows 15, access dinied"
    assert actual == expected

def test_old_enough_17():
    actual = verify_age("2007-2-1")
    expected = "Age verified, access granted"
    assert actual == expected    

def test_wrong_date_format():
    actual = verify_age("22/01/1990")
    with pytest.raises(Exception) as e:
        "The date of birth is in the wrong format, use the format YYYY-MM-DD"
    expected = e
    assert actual == expected    