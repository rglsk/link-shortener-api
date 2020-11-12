from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from api.deps import get_db  # noqa
from core.config import settings
from db.session import SessionLocal
from main import app
from models.links import Link
from models.stats import Stats


@pytest.fixture(scope="session")
def db():
    yield SessionLocal()


@pytest.fixture()
def client(db) -> Generator:
    def override_get_db():
        return db

    app.dependency_overrides[get_db] = override_get_db

    try:
        yield TestClient(app)
    finally:
        db.query(Link).delete()
        db.query(Stats).delete()
        db.commit()


@pytest.fixture()
def api_v1_str() -> str:
    return settings.API_V1_STR


@pytest.fixture()
def link_db(db: Session) -> Generator:
    link = Link(original_url="https://rogulski.it", domain="tier.app")
    db.add(link)
    db.commit()
    db.refresh(link)
    yield link
