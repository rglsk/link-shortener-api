from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import deps
from crud.link import create_db_link
from schemas.link import Link, LinkCreate

router = APIRouter()


@router.post("/links", response_model=Link, status_code=201)
def create_link(
    link_data: LinkCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    db_link = create_db_link(db, link_data)
    return Link(short_url=db_link.short_url)
