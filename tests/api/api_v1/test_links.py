import mock
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from models.links import Link


def test_create_link(client: TestClient, api_v1_str: str, db: Session):
    data = {"original_url": "https://rogulski-test.it", "domain": "tier.app"}

    response = client.post(f"{api_v1_str}/links", json=data)

    assert response.status_code == 201

    links = db.query(Link).all()
    assert len(links) == 1
    assert links[0].id in response.json()["short_url"]


@mock.patch("crud.link.generate_id")
def test_create_link_retry_id_collision(
    mock_generate_id,
    client: TestClient,
    api_v1_str: str,
    db: Session,
    link_db: Link,
):
    mock_generate_id.side_effect = [link_db.id, "123456789ab"]
    data = {"original_url": "https://rogulski-test.it", "domain": "tier.app"}

    response = client.post(f"{api_v1_str}/links", json=data)
    assert response.status_code == 201
    assert len(db.query(Link).all()) == 2
