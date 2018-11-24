from django.shortcuts import render
from django.shortcuts import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    @author: jack
    @modify: jack
    @return: 填一下
    """
    context = None
    template = loader.get_template('clock_in/index.html')
    return HttpResponse(template.render(context, request))
