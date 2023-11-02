from django.contrib import admin

from Customer.models import Customer
from Finance.models import Transaction
from users.models import InvalidLOgins, User

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(User)
admin.site.register(InvalidLOgins)