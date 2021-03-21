from django.shortcuts import render
from .models import Service

# Create your views here.

def service_index(request):


    return render(request, 'services/base_services.html')


def service_view(request, service_id):
    service = Service.objects.get(id=service_id)
    context = {"service" : service}
    return render(request, 'services/base_services.html', context=context)


