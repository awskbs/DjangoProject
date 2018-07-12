from django.http import HttpResponse
from django.shortcuts import render
from .models import bug_details
from implinks.models import implinks
def hello(request):
        bugs = bug_details.objects.all()
        links = implinks.objects.all()
        return render(request, 'bugDetails.html',{'bugs':bugs,'links':links})

# Create your views here.
