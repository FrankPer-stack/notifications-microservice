from utils.notifications import MessagingService
from models import SendNotificationRequest, Notification, NotificationType, PaginatedNotifications
from fastapi import APIRouter
from pydantic import conint
from typing import Optional
from uuid import UUID
from routes.notifications import controller


router = APIRouter(tags=["notifications"])
messaging_service = MessagingService()


@router.get("/notifications", response_model=PaginatedNotifications | Notification.Read)
async def get_notifications(
    page: conint(gt=0) = 1, # type: ignore
    size: conint(gt=0) = 50, # type: ignore
    id_notification: Optional[UUID] = None,
    key: Optional[str] = None,
    value: Optional[str] = None,
    search: Optional[str] = None,
    by_type: Optional[NotificationType] = None, 
    current_org: UUID = None,
):
    """
    # Usage:
    ### * Get all notifications: `/notifications?page=1&size=50&by_type=welcome`
    ### * Search notifications: `/notifications?search=Welcome to the locker app`
    ### * Get a single notification by ID: `/notifications?id_notification=UUID`
    ### * Filter by key-value pair: `/notifications?key=name&value=Welcome to the locker app`

    | Param           | Type              | Description                                | Return Type |
    |-----------------|-------------------|--------------------------------------------|-------------|
    | id_notification | UUID              | The unique ID of a notification            | Single      |
    | key             | str               | Field name to search by                    | Single      |
    | value           | str               | Value of the field to search by            | Single      |
    | search          | str               | General search term                        | List        |
    | by_type         | NotificationType   | Filter notifications by their type        | List        |
    """

    result = await controller.get_notifications(
        page=page,
        size=size,
        id_org=current_org,
        id_notification=id_notification,
        key=key,
        value=value,
        search=search,
        by_type=by_type,
    )
    return result

@router.post("/notifications", response_model=Notification.Read)
async def create_notification(
    notification: Notification.Write,
    current_org: UUID = None,
) -> Notification.Read:
    """
    # Usage:
    ### * Create a notification: `/notifications`
    
    | Param           | Type              | Description                                | Return Type |
    |-----------------|-------------------|--------------------------------------------|-------------|
    | notification    | Notification.Write| The notification to be created             | Single      |
    | current_org     | UUID              | The unique ID of the organization          | Single      |
    """

    result = await controller.create_notification(notification, current_org)
    return result


@router.post("/send-notification")
async def email_notification(request: SendNotificationRequest):
    """
    # Usage:
    ### * Send a notification: `/send-notification`

    | Param           | Type              | Description                                | Return Type |
    |-----------------|-------------------|--------------------------------------------|-------------|
    | request         | SendNotificationRequest | The notification to be sent          | Single      |
    """
    notification: Notification = await controller.get_notification(request.id_notification)
    return await messaging_service.send_notification(
        channels=request.channels,
        recipient=request.to,  
        message=notification.message
    )

@router.put("/notifications/{notification_id}")
async def update_notification(notification_id: int):
    pass

@router.delete("/notifications/{notification_id}")
async def delete_notification(notification_id: int):
    pass

