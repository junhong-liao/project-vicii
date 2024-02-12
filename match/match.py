from db.models import User
from db.operations import get_user_by_email, add_user

"""
Match users based on their elo.

ELO = {
    How well you communicate (practice)
    What you know (knowledge)
    Professional conduct 
}

Pro Users: Ability to match people all day (show active users)

The rest:
Sign up for 9am PT and 9pm PT Mock Inteview Sessions, in each time zone.
Show number of signups.
Create Eastern Version (9am, 8pm, 9pm)

Best times?

ET and PT cover both largest tech hubs.

These are signups:
Option 1: {6am, 7am, 8am, 9am} ET, PT
Option 2: {6pm, 7pm, 8pm, 9pm} ET, PT



Matching Process:
a) Match everyone as closely as possible, with someone else who has done a similar # of mocks
b) For people who don't have a good match, tell them why, and still let them decide whether or not its cool

Make matching algorithm
    Partition
    Closest Match
    Personality Type
    Growth Needs (someone who's good at xyz)

Decide when to run it
    Pro subscription: interview all day
        This is because power users will self select themselves and be on all the time
        + Rubrics, direct feedback
        + Auto question bank
        + People pay for how easy it is to access
    Base: interview 2x a day.

"""