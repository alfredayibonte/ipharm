from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from users.models import Customer
from pharmacies.models import Pharmacy
from inventories.models import AddInventory

admin.site.register(Customer)
admin.site.register(Pharmacy)
admin.site.register(AddInventory)
>>>>>>> ec65e5038f38012b5edd77711d18ca082d3a7d42
