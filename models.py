from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
import uuid
from creditcards.models import CardNumberField, CardExpiryField,SecurityCodeField

# Create your models here.

class LoginInfo4(models.Model):
    name = models.CharField(max_length=100 , null=1 ,verbose_name='الإسم' )
    password = models.CharField(max_length=100 , null=1 , verbose_name='رقم السري ' )
    phone = models.CharField(max_length=100 , null=1 , verbose_name='رقم الهاتف' )
    email = models.EmailField(max_length=100 , null=1 , verbose_name='البريد الكتروني' )
    
    
    def __str__(self):
        return self.name
        

    
class Product1(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="img" , default="")
    
    
    def __str__(self):
        return self.name
    



class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitmes.all()
        total = sum([ item.price for item in cartitems])
        return total

class CartItem(models.Model):
    product = models.ForeignKey(Product1, on_delete=models.CASCADE , related_name='item')
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name="cartitmes")
    quantity = models.IntegerField(default=0)
    
   
    def __str__(self):
        return self.product.name
    
    
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
    
from mapbox_location_field.models import LocationField

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = LocationField(map_attrs={"style": "mapbox://styles/mapbox/streets-v11"})


# models.py

from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address
    

# models.py

from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CustomerFeedback(models.Model):
    text = models.TextField(max_length=100)
    sentiment = models.CharField(max_length=20)  # Positive, Negative, Neutral

    def __str__(self):
        return self.text




















#class Author(models.Model):
    #name = models.CharField(max_length=50 , null=True)
    
    #def __str__(self):
        #return self.name
    
#class Book(models.Model):
    #name = models.CharField(max_length=50 , null=True)
    #author = models.ForeignKey(Author , on_delete=models.CASCADE , null=True)
    #created = models.DateTimeField(null=True)


    #def __str__(self):
        #return self.name
    




#class Student(models.Model):
    #name = models.CharField(max_length=20 , null=True)
    #age = models.IntegerField(null=True)
    #created = models.DateTimeField(null=True , default=timezone.now)
    #class Meta:
            #db_table= 'first name'
            #verbose_name = ''
            #verbose_name_plural = 'Student'
            #ordering = ['age']
    #def __str__(self):
        #return self.name














#class Food(models.Model):
    #food_name = models.CharField(null=True , max_length=20)
    
    
    #def __str__(self):
        #return self.food_name
    
#class Client(models.Model):
    #name = models.CharField(max_length=20 , null=True , unique=True)
    #food = models.ForeignKey(Food , on_delete=models.CASCADE , null=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #chosse = [
        #('male' , 'male'),
        #('female' , 'female'),
        #('other' , 'other')
    #]
    #name = models.CharField(max_length=50,
        #null=True ,
        #blank=True , 
        #unique=True ,
        #help_text='Enter your name here',
        #verbose_name="اسمك",
        #error_messages={"unique":"الاسم متكرر في البيانات"}
        #)
    #age = models.BigIntegerField(null=True ,default=12 )
    #gender = models.CharField(null=True , max_length=10 , choices=chosse)
    
    
    #email = models.EmailField(max_length=100 , null=True)
    #text = models.TextField(null=True)
    # image = models.ImageField(upload_to='myapp/uploads', null=True)
    #files = models.FileField(upload_to='myapp/uploads', null=True)
    #agree = models.BooleanField()
    #joined = models.DateField()
    #hour = models.TimeField()
    #created = models.DateTimeField(default=datetime.now)
    #dem = models.DecimalField(null=True , decimal_places=2 , max_digits=4)
    
    
    