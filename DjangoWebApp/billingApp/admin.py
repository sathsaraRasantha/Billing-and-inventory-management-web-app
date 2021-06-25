from django.contrib import admin
from billingApp.models import Bill_details, Customer,Bill, Service, Stock
# Register your models here.

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Bill)
admin.site.register(Bill_details)
admin.site.register(Stock)


