from django.db import models

# Create your models here.
class MarketGroup(models.Model):
    group_id = models.IntegerField(default=0, unique=True)
    parent_id = models.IntegerField(default=0, null=True)
    name = models.fields.CharField(max_length=200)
    icon_id = models.fields.IntegerField(default=0, null=True)
    has_types = models.fields.BooleanField(default=False)


class InvType(models.Model):
    type_id = models.fields.IntegerField(unique=True)
    group_id = models.fields.IntegerField(default=0)
    name = models.fields.CharField(max_length=200)
    volume = models.fields.DecimalField(default=0.00, decimal_places=2, max_digits=14)
    published = models.fields.BooleanField(default=False)
    icon_id = models.fields.IntegerField(default=0)
    graphic_id = models.fields.IntegerField(default=0)
    market_group = models.ForeignKey(MarketGroup, on_delete=models.DO_NOTHING, related_name='market_group', null=True)

    def __str__(self):
        return self.name

    @property
    def market_group_name(self):
        if self.market_group:
            return self.market_group.name
        else:
            return 'none'