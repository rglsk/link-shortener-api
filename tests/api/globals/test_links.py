from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from models.links import Link
from models.stats import Stats


def test_redirect_link(client: TestClient, db: Session, link_db: Link):
    url = f"/{link_db.id}"
    response = client.get(url)

    assert response.history[0].status_code == 307
    assert response.history[0].url.endswith(url)

    stats = db.query(Stats).all()
    assert len(stats) == 1
    assert stats[0].link_id == link_db.id


def test_redirect_link_not_found(client: TestClient, db: Session):
    url = f"/12345678900"
    response = client.get(url)

    assert response.status_code == 404
    stats = db.query(Stats).all()
    assert len(stats) == 0
