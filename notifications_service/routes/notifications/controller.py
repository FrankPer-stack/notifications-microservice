import logging
from typing import Optional
from uuid import UUID
from fastapi_async_sqlalchemy import db
from pydantic import conint
from sqlalchemy import VARCHAR, cast, delete, insert, or_, select, update
from models import Notification, NotificationType, PaginatedNotifications
from utils.api_func import _get_paginated_query, _get_by_key_value

 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


async def get_notification(id_notification: UUID):
    query = select(Notification).where(Notification.id == id_notification)
    result = await db.session.execute(query)
    notification = result.unique().scalar_one()
    return notification


async def get_notifications(
    page: conint(gt=0), # type: ignore
    size: conint(gt=0), # type: ignore
    id_org: UUID,
    id_notification: Optional[UUID] = None,
    key: Optional[str] = None,
    value: Optional[str] = None,
    search: Optional[str] = None,
    by_type: Optional[NotificationType] = None,
):
    query = select(Notification).where(Notification.id_org == id_org)
    query_response = await db.session.execute(query)
    notifications = query_response.unique().scalars().all()

    if id_notification:
        notification = get_notification(id_notification, id_org)
        return notification

    if key and value:
        notification = await _get_by_key_value(key, value, id_org)
        return notification

    if search:
        query = query.where(
            or_(
                Notification.name.ilike(f"%{search}%"),
                Notification.message.ilike(f"%{search}%"),
            )
        )

    if by_type:
        query = query.where(Notification.notification_type == by_type)

    totals, notifications_paginated = await _get_paginated_query(
        results=notifications, page=page, size=size
    )

    return PaginatedNotifications(totals=totals, items=notifications_paginated)



async def create_notification(
    notification: Notification.Write,
    id_org: UUID,
) -> Notification.Read:
    new_notification = Notification(
        name=notification.name,
        message=notification.message,
        member_message=notification.member_message,
        mode=notification.mode,
        notification_type=notification.notification_type,
        time_amount=notification.time_amount,
        time_unit=notification.time_unit,
        before=notification.before,
        after=notification.after,
        email=notification.email,
        sms=notification.sms,
        push=notification.push,
        email_2nd=notification.email_2nd,
        sms_2nd=notification.sms_2nd,
        push_2nd=notification.push_2nd,
        is_template=notification.is_template,
        id_member=notification.id_member,
        recipient_type=notification.recipient_type,
    )

    query = (
        insert(Notification)
        .values(**new_notification.dict(), id_org=id_org)
        .returning(Notification)
    )

    response = await db.session.execute(query)
    inserted_notification = response.unique().all().pop()
    await db.session.commit()

    return inserted_notification




