from datetime import datetime, UTC
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

from events import EventBus, EventType

router = APIRouter()


class ShortLinkCreate(BaseModel):
    target_url: HttpUrl


class ShortLink(BaseModel):
    id: UUID
    short_code: str
    target_url: HttpUrl
    clicks: int = 0


links: dict[str, ShortLink] = {}


def configure(bus: EventBus):
    global event_bus
    event_bus = bus


@router.post("/links")
def create_short_link(data: ShortLinkCreate) -> ShortLink:
    short_code = uuid4().hex[:6]

    link = ShortLink(
        id=uuid4(),
        short_code=short_code,
        target_url=data.target_url,
    )

    links[short_code] = link
    if event_bus is not None:
        event_bus.publish(
            EventType.LINK_CREATED,
            data={
                "type": "link.created",
                "link_id": str(link.id),
                "short_code": link.short_code,
                "target_url": str(link.target_url),
            },
        )

    return link


@router.get("/links")
def list_short_links() -> list[ShortLink]:
    return list(links.values())


@router.get("/{short_code}")
def redirect_to_target(short_code: str) -> RedirectResponse:
    link = links.get(short_code)

    if link is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    link.clicks += 1
    if event_bus is not None:
        event_bus.publish(
            EventType.LINK_CLICKED,
            data={
                "type": "link.clicked",
                "link_id": str(link.id),
                "short_code": link.short_code,
                "target_url": str(link.target_url),
                "clicks": link.clicks,
                "clicked_at": datetime.now(UTC).isoformat(),
            },
        )

    return RedirectResponse(str(link.target_url))
