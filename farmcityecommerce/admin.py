from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'method', 'amount', 'approved', 'created_at')
    list_filter = ('approved', 'method')
    actions = ['approve_payments']

    def approve_payments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected payments have been approved.")
    approve_payments.short_description = "Approve selected payments"