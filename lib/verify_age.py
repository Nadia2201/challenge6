from datetime import datetime

def verify_age(date):
    try:
        today = datetime.now()
        dob = datetime.strptime(date, '%Y-%m-%d')
        age = today.year - dob.year
        if age < 16:
            return f"Age shows {age}, access dinied"
        else:
            return "Age verified, access granted"
    except ValueError:
        raise Exception("The date of birth is in the wrong format, use the format YYYY-MM-DD")




