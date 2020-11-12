from typing import Generator

from db.session import SessionLocal


def get_db() -> Generator:  # pragma: no cover
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
