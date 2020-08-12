from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    
def ready(self):
    '''
    Import signals, so when any line of the order
    is deleted or updated,
    the order will be updated as well
    '''
    import checkout.signals
