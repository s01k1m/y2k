from django.shortcuts import render
from .models import Still
from django.shortcuts import get_list_or_404, get_object_or_404

def still_list(request):
    still_list = get_list_or_404(Still)
    print(still_list)

def still_of_color(request, colorChoice):
    still_of_color_list = get_list_or_404(Still, still_color=colorChoice)
    print(still_of_color_list)