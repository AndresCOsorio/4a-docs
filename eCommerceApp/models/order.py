from django.db import models
from django.utils import timezone
from eCommerceApp.models.user import User


class Order(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    send_type = models.CharField('Tipo envio', max_length=100, null=False)
    send_price = models.CharField('Gasto envio', max_length=100, null=False)
    total_charge = models.IntegerField('Cargo total', null=False)
    order_status = models.CharField('Estado orden', max_length=100)
    pay = models.IntegerField('Pago', null=False)
    pay_type = models.CharField('Tipo pago', max_length=100)
    order_detail = models.IntegerField('Id Detalle', null=False)
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.DO_NOTHING)
