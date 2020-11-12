import datetime
import random
import string

from sqlalchemy import Column, String, DateTime

from db.base_class import Base


def generate_id(size=11):
    """Generate a random string of letters and digits"""
    letters_and_digits = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(size))


class Link(Base):
    id = Column(String, primary_key=True, index=True, unique=True, default=generate_id)
    original_url = Column(String)
    domain = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def short_url(self):
        return f"{self.domain}/{self.id}"
