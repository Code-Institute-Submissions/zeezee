from django.db import models


class SendBack(models.Model):
    '''
    Let the user send the order number
    and a justification, so the shop owner
    can handle request in admin
    '''
    name = models.CharField(max_length=80)
    email = models.EmailField()
    reason = models.TextField()
    order_number = models.CharField(max_length=80)

