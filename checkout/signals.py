from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Handle signals, and update the order on save
    Receiver decorator to execute the function itself
    receiving post_save signals from the sender, in this case
    the OrderLineItem
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the total when it's saved
    OrderLineItem model, the line of the order
    and keyword arguments as parameters
    """
    instance.order.update_total()
