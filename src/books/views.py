# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view instead of a clas a
# render take 3 arguments:
# 1- the request
# 2- a template
# 3- a Context for the template as dict
def home(request):
    return HttpResponse("Hello")
    #return render(request, "home.html", {})
