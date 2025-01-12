from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    # return HttpResponse("Site of application")
    return render(request, 'second_task/func_template.html')


class Index(TemplateView):
    template_name = 'second_task/class_template.html'
