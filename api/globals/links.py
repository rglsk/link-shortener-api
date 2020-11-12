from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from api import deps
from crud.link import get_db_link_by_short_url
from crud.stats import create_stats

router = APIRouter()


@router.get("/{link_id}")
def redirect_link(link_id: str, db: Session = Depends(deps.get_db)) -> Any:
    # TODO: Add cache (redis)
    db_link = get_db_link_by_short_url(db, link_id)
    if not db_link:
        raise HTTPException(status_code=404, detail="Link not found")

    create_stats(db, db_link.id)  # TODO: Make it async
    return RedirectResponse(db_link.original_url)
