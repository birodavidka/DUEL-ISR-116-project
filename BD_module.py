import re

def bd_format_email(email: str) -> str:
    return email.strip().lower()

def bd_validate_email(email: str) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))

def bd_mask_password(pw: str) -> str:
    return "*" * len(pw)

class BDUser:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
    def to_dict(self) -> dict:
        return {"email": self.email, "password": self.password}
    def __repr__(self) -> str:
        return f"BDUser(email={self.email}, password={bd_mask_password(self.password)})"
