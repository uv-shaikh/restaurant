from django.contrib import admin
from .models import Category
from .models import Product
from .models import Signup
from .models import Table
from .models import bookingdate
from .models import Mycart

admin.site.site_header="developer Uv"
admin.site.site_title="Welcome to Uv Deshboard"
admin.site.index_title="Welcome to This Portal"

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Table)
admin.site.register(bookingdate)
admin.site.register(Mycart)

# Register your models here.
