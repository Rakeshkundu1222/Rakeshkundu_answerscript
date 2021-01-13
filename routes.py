from django.http import HttpResponse
from .models import Users
from .models import Addresses

def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    try:
        user = User()
        user.username = username
        user.password = password
        user.save()
        # Ideally should return authentication token
        return HttpResponse(status=201)
    except:
        return HttpResponse(status=500)

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = Users.objects.get(username = username)
    if user.password == password:
        # Ideally should return authentication token
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)
    
def add_address(request):
    username = request.POST.get('username', '')

    street = request.POST.get('street','')
    pincode = int(request.POST.get('pincode',''))
    country = request.POST.get('country','')
    state = request.POST.get('state','')
    phone = int(request.POST.get('phone',''))

    try:
        address = Addresses()
        address.username = username
        address.street = street
        address.pincode = pincode
        address.country = country
        address.state = state
        address.phone = phone
        address.save()
        return HttpResponse(status=201)
    except:
        return HttpResponse(status=500)

def update_address(request):
    username = request.POST.get('username', '')

    street = request.POST.get('street','')
    pincode = int(request.POST.get('pincode',''))
    country = request.POST.get('country','')
    state = request.POST.get('state','')
    phone = int(request.POST.get('phone',''))

    try:
        address = Addresses.objects.get(username = username)
        address.username = username
        address.street = street
        address.pincode = pincode
        address.country = country
        address.state = state
        address.phone = phone
        address.save()
        return HttpResponse(status=201)
    except:
        return HttpResponse(status=500)
    
