from pydantic import BaseModel, AnyHttpUrl


class LinkBase(BaseModel):
    original_url: AnyHttpUrl
    domain: str


class LinkCreate(LinkBase):
    pass


class LinkInDB(LinkBase):
    id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Link(BaseModel):
    short_url: str
