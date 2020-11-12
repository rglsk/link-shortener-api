import sqlalchemy.orm.exc
from sqlalchemy.orm import load_only
from sqlalchemy.orm import Session

from schemas.link import LinkCreate
from models.links import Link, generate_id
from retrying import retry


@retry(stop_max_attempt_number=100)
def create_db_link(db: Session, link: LinkCreate):
    db_link = Link(
        id=generate_id(),
        original_url=link.original_url,
        domain=link.domain,
    )
    db.add(db_link)
    try:
        db.commit()
    except sqlalchemy.orm.exc.FlushError:
        db.rollback()
        raise
    db.refresh(db_link)
    return db_link


def get_db_link_by_short_url(db: Session, link_id: str) -> Link:
    link = db.query(Link).options(load_only(Link.original_url)).get(link_id)
    return link
