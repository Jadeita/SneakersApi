import http
from msilib.schema import Dialog
from ssl import AlertDescription
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.urls import reverse
from django.contrib import messages

from .connectionOdoo import connectionOdoo
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.db import IntegrityError

# REGISTRO.
def register(request):
    if request.method == "POST": 

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        try:

            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:

            return HttpResponse("<h2> Username taken </h2><br><br> <a href= ''>Return</a> ")
            
        login(request, user)

        return HttpResponseRedirect(reverse("index"))

    else:

        return render(request, "crud/register.html")

# INICIAR SESIÓN

def loginview(request):

    if request.method == 'POST':

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password) 

        if user is not None: #sí existe el usuario
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request,'username or password not correct')    
            
    return render(request, "crud/login.html")




# CERRAR SESIÓN

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("register"))



def index(request):
    
    odoo = connectionOdoo()
    
    products =  odoo.models.execute_kw(odoo.db,odoo.uid,odoo.password,
    'product.template','search_read',
        [
            [
                
                [ "company_id" ,"=", 1   ]
                # [ "id" ,"=", 2]
            ]
        ],
        {'fields': ["name", "list_price", "default_code","description_picking"]}
    )
 

    return render(request, "crud/index.html", {"abarrotes": products})
