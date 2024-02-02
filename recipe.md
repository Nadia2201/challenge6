# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_verify(date_of_birth):
    """Verifies if a user is old enough to be granted access

    Parameters: (list all parameters and their types)
        date_of_birth: a string in adate format YYYY-MM_DD

    Returns: (state the return value and its type)
        a positive string if over 16 "Age verified, access granted"
        a negative string if under 16 "Age shows {age}, access dinied"
        an error message if the date is in the wrong format "The date of birth is in the wrong format, use the format YYYY-MM-DD"

    Side effects: (state any side effects)
        This function prints different messages depending on the user's input
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given age under 15
It returns "Age shows 15, access dinied"
"""
age_verify("2009-2-1") => "Age shows 15, access dinied"

"""
Given age 17
It returns "Age verified, access granted"
"""
age_verify("2007-2-1") => "Age verified, access granted"

"""
Given 22/01/1990
It returns "The date of birth is in the wrong format, use the format YYYY-MM-DD"

"""
age_verify("22/01/1990") => "The date of birth is in the wrong format, use the format YYYY-MM-DD"



"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.age_verify import *
import pytest
"""
Given age under 15
It returns "Age shows 15, access dinied"
"""
    def test_under_age():
        actual = age_verify("2009-2-1") 
        expected = "Age shows 15, access dinied"
        assert actual == expected

"""
Given age 17
It returns "Age verified, access granted"
"""
    def test_old_enough():
        actual = age_verify("2007-2-1")
        expected = "Age verified, access granted"
        assert actual == expected

"""
Given 22/01/1990
It returns "The date of birth is in the wrong format, use the format YYYY-MM-DD"

"""
    def test_wrong_date_format():
        actual = age_verify("22/01/1990")
        with pytest.raises(Exception) as e:
            "The date of birth is in the wrong format, use the format YYYY-MM-DD"
        expected = str(e.value)
        assert actual == expected


```

Ensure all test function names are unique, otherwise pytest will ignore them!
