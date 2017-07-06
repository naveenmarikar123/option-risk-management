from django.db import models

# Create your models here.


class OptionChain(models.Model):
	open_interest = models.FloatField(null=True, blank=True, default=None)
	change_open_interest = models.FloatField(null=True, blank=True, default=None)
	strike_price = models.FloatField(null=True, blank=True, default=None)
	spot_price = models.FloatField(null=True, blank=True, default=None)
	volatility = models.FloatField(null=True, blank=True, default=None)
	last_traded_price = models.FloatField(null=True, blank=True, default=None)
	created_on = models.DateField(null=True, blank=True, default=None)
	stock_symbol = models.CharField(max_length=100 , null=True,blank=True,default=None)

	def __str__(self):
		return str(self.open_interest) + '-' + str(self.change_open_interest) + '-' + str(self.strike_price)
