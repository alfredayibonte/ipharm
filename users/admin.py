from django.contrib import admin
from users.models import Customer
from pharmacies.models import Pharmacy
from inventories.models import Drug

admin.site.register(Customer)
admin.site.register(Pharmacy)
admin.site.register(Drug)