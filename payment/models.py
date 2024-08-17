from django.db import models
from django.contrib.auth.models import User


class PaymentTitleModel(models.Model):
    title = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PaymentModel(models.Model):
    user = models.ForeignKey(User, db_column='user', on_delete=models.SET_DEFAULT, default='user-deleted')
    title = models.ForeignKey(PaymentTitleModel, on_delete=models.SET_DEFAULT, default='title-deleted', related_name='rel_payment_title')
    is_paid = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title}'
