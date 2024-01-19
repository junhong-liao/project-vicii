from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    # need frontend to set this user up
    # update username with a call, but leave empty?
    # generate a random username?
    username: Optional[str] = None
    email: EmailStr
    elo: int = 1000