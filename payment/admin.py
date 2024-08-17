from django.contrib import admin
from .models import PaymentModel, PaymentTitleModel


@admin.register(PaymentTitleModel)
class PaymentTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'updated', 'created')
    ordering = ('updated', 'created')
    readonly_fields = ('updated', 'created')


@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_paid', 'updated', 'created')
    list_filter = ('user', 'is_paid', 'title')
    ordering = ('updated', 'created')
    readonly_fields = ('updated', 'created')
