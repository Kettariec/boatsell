from boat.models import Boat
from django.core.mail import send_mail
from order.models import Order
from django.conf import settings


def send_order_email(order_item: Order):
    send_mail(
        'Заказ на покупк лодки',
        f'{order_item.name} ({order_item.mail}) хочет купить '
        f'вашу лодку {order_item.boat.name}. '
        f'Сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.boat.owner.email]
    )
