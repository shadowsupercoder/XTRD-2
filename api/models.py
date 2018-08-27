from django.db import models


TOTAL_SUPPLY = 952457688


class XTRDInformation(models.Model):
    """XTRD Information abstract model
    price in USD
    """
    date = models.DateTimeField(
        null=True,
        auto_now_add=True,
        editable=False)
    price_usd = models.DecimalField(
    	max_digits=1000,
    	decimal_places=5,
    	verbose_name='USD')
    price_eth = models.DecimalField(
        max_digits=1000,
        decimal_places=18,
        verbose_name='ETH')
    volume = models.DecimalField(
    	max_digits=1000,
    	decimal_places=18,
    	verbose_name='Volume')

    # TODO trade volume

    class Meta:
        abstract = True

    def get_market_cap(self):
    	return TOTAL_SUPPLY * self.price

    @property
    def supply(self):
        return TOTAL_SUPPLY


class Etherscan(XTRDInformation):
    """XTRD Information on Etherscan"""
    pass


class Coinmarketcap(XTRDInformation):
    """XTRD Information on Coinmarketcap"""
    pass