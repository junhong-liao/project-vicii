from db.models import User
from db.operations import get_user_by_email, add_user

"""
Match users based on their elo.

# elo is tough to define. an elo that breaks down fundamental skills by industry could be better.

ELO = {
    How well you communicate (practice),
    What you know (knowledge),
    Deameanor (professionalism, 'culture fit')
}

The TYPE of mock interview you're signed up for matters too

For example,

PM.ELO = {
    Communication,
    User Centricity,
    Structure of Thought,
    Empathy (Users, EQ),
    Collaboration,
    Creativity
}

Each of these factors should have a weight, and can aggregate to total value
this total value represents the ELO for that particular skill.

So while each ELO function for PM vs SWE vs Consulting is different, we can use the individual's fundamnetal abilities to match them

As in, if MBB consulting interviews look for Communication, Strategy, and Analytical Thinking, and SWE needs Analytical Thinking, Communication, and Math, for example,
Then we could calculate the consulting elo of an engineer, for example.

Weights are in place to ensure that your ELO can't be carried by just one factor alone.

Matching based on this elo system will take place based on signups.

I think for MVP, we should match people beforehand, and show them when their partner is on. If their partner is NOT on, they can request a rematch.
    This requires 'rematch' functionality to be built

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

--

Matching Process:
a) Match everyone as closely as possible, with someone else who has done a similar # of mocks
b) For people who don't have a good match, tell them why, and still let them decide whether or not its cool

Make matching algorithm:
    Partition
    Closest Match
    Personality Type
    Growth Needs (someone who's good at xyz)

Decide when to run it:
    Pro subscription: interview all day
        This is because power users will self select themselves and be on all the time
        + Rubrics, direct feedback
        + Auto question bank
        + People pay for how easy it is to access

    Base membership: interview 2x a day
        + Cost: a google account

"""