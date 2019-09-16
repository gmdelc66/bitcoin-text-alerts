from django.db import models
from django.contrib.auth.models import User


# create profile model to collect contact information about users
# use django user model to authenticate, profile to ... profile
class Alert(models.Model):

    BITCOIN = 'BTC'
    ETHEREUM = 'ETH'
    AUGUR = 'REP'
    MAKER = 'MKR'
    USD = 'USD'
    EUROS = 'EUR'

    QUOTE_CURRENCY_CHOICES = [
        (BITCOIN, 'Bitcoin'),
        (ETHEREUM, 'Ethereum'),
        (AUGUR, 'Augur'),
        (MAKER, 'Maker')
    ]
    BASE_CURRENCY_CHOICES = [
        (USD, 'US Dollars'),
        (EUROS, 'Euros')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_currency = models.CharField(max_length=64, blank=False,
                                      choices=QUOTE_CURRENCY_CHOICES)
    base_currency = models.CharField(max_length=64, blank=False,
                                     choices=BASE_CURRENCY_CHOICES)
    alert_count = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'A daily alert with the price of {self.quote_currency} in {self.base_currency}'
