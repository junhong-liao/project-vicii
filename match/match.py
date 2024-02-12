from db.models import User
from db.operations import get_user_by_email, add_user

"""
Match users based on their elo.

ELO = A function of
    How well you communicate (practice)
    What you know (knowledge)
    Professional conduct 


Pro Users: Ability to match people all day (show active users)

The rest:
Sign up for 9am PT and 9pm PT Mock Inteview Sessions, in each time zone.
Show number of signups.
Create Eastern Version (9am, 8pm, 9pm)

Best times?

Option 1: {6am, 7am, 8am, 9am}
Option 2: {6pm, 7pm, 8pm, 9pm}


If there are online users that are += 10 
If there is someone anyone in the same 'rating bucket', you can be matched




"""