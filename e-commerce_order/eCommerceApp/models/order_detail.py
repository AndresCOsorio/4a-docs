from django.db import models
from eCommerceApp.models.user import User


class OrderDetail(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    ord_detail = models.BigIntegerField("order_detail", null=False)
    amount_prod = models.IntegerField('Amount Product', null=False)
    id_prod = models.IntegerField('Id Product', null=False)
    id_user = models.ForeignKey(User, related_name='order_detail_user', on_delete=models.DO_NOTHING)

