from enum import Enum
import uuid

class Role(Enum):
    ADMIN = "Admin"
    USER = "User"
    RIDER = "Rider"

class User:
    def __init__(self, username, role: Role):
        self.username = username
        self.role = role

    def __str__(self):
        return f"{self.role.value}({self.username})"