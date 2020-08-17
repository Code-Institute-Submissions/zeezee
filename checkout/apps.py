from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    ''''
    Import signals, so when any line of the order
    is deleted or updated,
    the order will be updated as well
    '''
    name = 'checkout'

    def ready(self):
        import checkout.signals
