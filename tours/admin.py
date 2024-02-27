from django.contrib import admin
from .models import *

admin.site.register(TourCategories)
admin.site.register(Tours)
admin.site.register(Reservation)
admin.site.register(Reviews)

# Register your models here.
