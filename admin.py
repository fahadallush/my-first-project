from django.contrib import admin
from myapp import models
from .models import *
# Register your models here.


admin.site.register([Product1 , Cart , CartItem])

#admin.site.register(models.Student)

#admin.site.register(models.Author)

#admin.site.register(models.Book)
