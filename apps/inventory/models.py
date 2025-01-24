from django.db import models

from apps.app.models import InvType


class Asset(models.Model):
    type = models.ForeignKey(InvType, on_delete=models.DO_NOTHING)
    character = models.IntegerField(default=0)
    item_id = models.BigIntegerField(default=0)
    location_id = models.BigIntegerField(default=0)
    location_type = models.CharField(max_length=200, null=True)
    location_flag = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.type.name

    @property
    def item_name(self):
        return self.type.name


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['type', 'location_id'], name='unique_asset_constraint')
        ]