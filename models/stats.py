import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from db.base_class import Base


class Stats(Base):
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    link_id = Column(
        String,
        ForeignKey("link.id", ondelete="CASCADE"),
    )
