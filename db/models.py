from pydantic import BaseModel, EmailStr
from typing import Optional

"""
need frontend to set this user up
update username with a call, but leave empty?
generate a random username?
"""
class User(BaseModel):
    username: Optional[str] = None
    email: EmailStr
    elo: int