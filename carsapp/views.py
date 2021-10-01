from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Booking,Contact
from carsapp.models import Contact as addcontact

def Index(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        model = request.POST['model']
        departuredate= request.POST['departuredate']
        returndate = request.POST['returndate']
        booking_obj = Booking(name = name,email = email,phone = phone,model = model,departuredate = departuredate, returndate  = returndate)
        booking_obj.save()
        print("your application as be submitted")
    return render(request,'index.html')



class About(TemplateView):
    model = Booking
    template_name = 'about.html'


class Servies(TemplateView):
    model = Booking
    template_name = 'servies.html'

def Contact(request):
    print("data as be submitted")
    if request.method == 'POST':
        firstname = request.POST.get('firstname',False)
        lastname  = request.POST.get('lastname',False)
        phone      = request.POST.get('phone',False)
        email      = request.POST.get('email',False)
        message    = request.POST.get('message',False)

        contact_obj = addcontact(firstname = firstname, lastname = lastname, phone = phone, email = email, message = message)
        contact_obj.save()

    return render(request,'contact.html')

