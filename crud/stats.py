from sqlalchemy.orm import Session

from models.stats import Stats
from retrying import retry


@retry(stop_max_attempt_number=100)
def create_stats(db: Session, link_id: str):
    db_stats = Stats(link_id=link_id)
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats
