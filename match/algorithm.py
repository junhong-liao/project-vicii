from db.models import User
from db.operations import get_user_by_email, add_user

def categorize_user_into_tier(user):
    if user.elo_rating < 1200:
        return 'beginner'
    elif user.elo_rating < 1800:
        return 'intermediate'
    else:
        return 'advanced'

def find_match_for_user_in_tier(current_user):
    user_tier = categorize_user_into_tier(current_user)
    matched_users = query_database("SELECT * FROM users WHERE elo_tier = user_tier")
    return matched_users
