from django.http import HttpResponse , FileResponse , JsonResponse
from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from . models import LoginInfo4
from myapp.forms import LoginInfo3 , PlaceForm
from django.contrib import messages , auth
import plotly
import plotly.express as px
import json
import matplotlib.pyplot as plt
from django_pandas.io import read_frame
import plotly.graph_objs as go
from myapp.models import CartItem , Product1 , Cart
from django.contrib.auth.models import User
import json

def details(request):
    all_data = LoginInfo4.objects.all()
    print(all_data)
    return render(request , 'myapp/details.html' , {'all_data': all_data})

def cart(request):
    
    cart = None
    cartitems= []
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitmes.all()
    
    
    
    
    context = {
        "cart":cart, "items":cartitems
    }
    return render(request, 'myapp/cart.html', context=context)

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product1.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user , completed=False)
        cartitem , created = CartItem.objects.get_or_create(cart=cart , product=product)
        cartitem.quantity += 1 
        cartitem.save()
        print(cartitem)
        
    return JsonResponse("it is working", safe=False)


    
def save_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

            if cart.save():
                cart.completed=True
            messages.success(request, "تم الدفع بنجاح")
        else:
            messages.error(request, "تحتاج إلى تسجيل دخول ")
        cart = None
        cartitems= []
        return redirect('/')   
    else:
        # If the request method is not POST, redirect to the cart page
        return redirect('cart')


def Payment(request):
    context = None
    
    pass    
    return render(request , 'myapp/pay.html')
def about(request):
    return render(request , 'myapp/about.html' )

def home1 (request):
    products= Product1.objects.all()
    context = {
        "products":products
    }
    
    return render(request , 'myapp/home.html', context=context)


def Offers(request):
    return  render (request , 'myapp/Offers.html' ,  {})

def ournews(request):
    return render (request , 'myapp/ournews.html' , {})

def Meals(request):
    return render (request , 'myapp/Meals.html' , {})

def burgers(request):
    return render (request , 'myapp/burgers.html' , {})

def potato(request):
    return render (request , 'myapp/potato.html' , {})

def piessection(request):
    return render (request , 'myapp/piessection.html' , {})

def sweets(request):
    return render (request ,  'myapp/sweets.html' , {})

def Drinks(request):
    return render (request , 'myapp/Drinks.html' , {})


def Dashboard(request):
    x1 = CartItem.objects.all()

    df = read_frame(x1)

    name = df['product']
    sells = df['quantity']

    data = {
        "x": name,
        "y": sells,
        "type": "bar"
    }

    layout = {
        "title": "الاكثر مبيعاً",
        "xaxis": {
            "title": "المنتج"
        },
        "yaxis": {
            "title": "عدد البيع"
        }
    }

    plotly_json = json.dumps({"data": [data], "layout": layout}, cls=plotly.utils.PlotlyJSONEncoder)


    all_data = Product1.objects.all()
    context = {
        "plotly_json": plotly_json,
        "all_data": all_data,
    }


    return render(request, 'myapp/Dashboard.html', context=context)



# views.py

# views.py

import requests
from django.shortcuts import render
from .forms import AddressForm

def address_autofill(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            access_token = 'pk.eyJ1IjoiZmFoYWRhaWwiLCJhIjoiY2x3NXRxZzB2MWZ5bzJpcGhjd2JmNW0ybSJ9.Kgi87E5-OQWYJRBnf3iEYw'
            url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={access_token}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Extract coordinates from response
                coordinates = data['features'][0]['geometry']['coordinates']
                context = {'form': form, 'coordinates': coordinates}
                return render(request, 'myapp/map.html', context=context)
            else:
                # Handle error
                pass
    else:
        form = AddressForm()
    return render(request, 'myapp/map.html', {'form': form})

# views.py

import requests
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_text = form.cleaned_data['text']
            sentiment = analyze_sentiment(feedback_text)
            feedback = form.save(commit=True)
            feedback.sentiment = sentiment
            feedback.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    form = FeedbackForm()
    return render(request, 'myapp/Technicalsupport.html', {'form': form})


            
   

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'






