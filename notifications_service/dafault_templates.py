from models import EventType, Notification, NotificationType, TimeUnit

# ------------------------------------
# Service Notifications Group
# ------------------------------------

SERVICE_PICKUP = Notification.Write(
    name="Picked up",
    message="Good news! Your items have been picked up and are being processed for order ((order_id)). We'll soon weigh it and let you know how much will be charged to your card.",
    mode=EventType.service,
    notification_type=NotificationType.on_service_pickup,
    time_amount=0,
    time_unit=TimeUnit.immediately,
    before=False,
    after=True,
    email=False,
    sms=True,
    push=False,
    is_template=True,
    id_member=None,
)
SERVICE_READY_PICKUP = Notification.Write(
    name="Ready for pick-up",
    message="Your items are ready for pickup! Your Order ID is ((order_id)). We will update you soon when we pick them up from ((location_name))",
    mode=EventType.service,
    notification_type=NotificationType.on_start,
    time_amount=0,
    time_unit=TimeUnit.immediately,
    before=False,
    after=True,
    email=False,
    sms=True,
    push=False,
    is_template=True,
    id_member=None,
)
SERVICE_CHARGE = Notification.Write(
    name="Charge",
    message="Your items weigh ((weight)) ((unit)) and you were successfully charged ((currency))((amount)) for order ((order_id)). Your order is in process and we will notify you when it's available to be picked up.",
    mode=EventType.service,
    notification_type=NotificationType.on_service_charge,
    time_amount=0,
    time_unit=TimeUnit.immediately,
    before=False,
    after=True,
    email=False,
    sms=True,
    push=False,
    is_template=True,
    id_member=None,
)
SERVICE_DROPOFF = Notification.Write(
    name="User Pickup",
    message="Your fresh laundry is ready to be picked up in locker ((locker_number)) for order ((order_id)). Please retrieve as soon as possible from ((location_address)). Use this link ((URL)) to unlock the locker and retrieve your items.",
    mode=EventType.service,
    notification_type=NotificationType.on_service_dropoff,
    time_amount=0,
    time_unit=TimeUnit.immediately,
    before=False,
    after=True,
    email=False,
    sms=True,
    push=False,
    is_template=True,
    id_member=None,
)
SERVICE_ON_COMPLETE = (
    Notification.Write(
        name="Complete",
        message="Order ((order_id)) has been completed. Thank you for trusting us with your ((service)). Please return soon!",
        mode=EventType.service,
        notification_type=NotificationType.on_complete,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)

SERVICE_NOTIFICATIONS = [
    SERVICE_PICKUP,
    SERVICE_READY_PICKUP,
    SERVICE_CHARGE,
    SERVICE_DROPOFF,
    SERVICE_ON_COMPLETE,
]

# ------------------------------------
# Rental Notifications Group
# ------------------------------------

RENTAL_ON_START = (
    Notification.Write(
        name="Transaction Starts",
        message="Order ((order_id)) has started in locker ((locker_number)) at ((location_name)). ((location_address)). You may also view your order at any time from the app.",
        mode=EventType.rental,
        notification_type=NotificationType.on_start,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)
RENTAL_ON_COMPLETE = (
    Notification.Write(
        name="Complete",
        message="Order ((order_id)) has successfully been completed. Thank you for using our service. Please return soon!",
        mode=EventType.rental,
        notification_type=NotificationType.on_complete,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)

RENTAL_NOTIFICATIONS = [RENTAL_ON_START, RENTAL_ON_COMPLETE]

# ------------------------------------
# Storage Notifications Group
# ------------------------------------

STORAGE_ON_START = (
    Notification.Write(
        name="Transaction Starts",
        message="Order ((order_id)) has started in locker ((locker_number)) at ((location_name)). ((location_address))",
        mode=EventType.storage,
        notification_type=NotificationType.on_start,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)
RENTAL_ON_COMPLETE = (
    Notification.Write(
        name="Complete",
        message="Order ((order_id)) has successfully been completed. Thank you for trusting us. Please return soon! ",
        mode=EventType.storage,
        notification_type=NotificationType.on_complete,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)

STORAGE_NOTIFICATIONS = [STORAGE_ON_START, RENTAL_ON_COMPLETE]

# ------------------------------------
# Delivery Notifications Group
# ------------------------------------

DELIVERY_ON_START = (
    Notification.Write(
        name="User Pick Up",
        message="Your transaction has started in locker ((locker_number)) at ((location_name)), ((location_address)). Use this event code ((event code)) to access the locker.",
        mode=EventType.delivery,
        notification_type=NotificationType.on_start,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)
DELIVERY_ON_COMPLETE = (
    Notification.Write(
        name="Complete",
        message="Order ((order_id)) has successfully been completed. Thank you for trusting us. Please return soon! ",
        mode=EventType.delivery,
        notification_type=NotificationType.on_complete,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)
DELIVERY_ON_EXPIRED = (
    Notification.Write(
        name="Expired Package",
        message="Your parcel is going to expire in ((selected_duration)) from ((locker_number)) at ((location_name)). If you do not collect your parcel before it expires you can collect it from the front desk.",
        mode=EventType.delivery,
        notification_type=NotificationType.on_expired,
        time_amount=0,
        time_unit=TimeUnit.immediately,
        before=False,
        after=True,
        email=False,
        sms=True,
        push=False,
        email_2nd=False,
        sms_2nd=False,
        push_2nd=False,
        is_template=True,
        id_member=None,
    ),
)

DELIVERY_NOTIFICATIONS = [DELIVERY_ON_START, DELIVERY_ON_COMPLETE, DELIVERY_ON_EXPIRED]