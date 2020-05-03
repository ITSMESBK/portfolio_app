# ========================================================================================
# ! /usr/bin/env python
# Filename: views.py

# Description:Adding Functionality to the WebApp

# Author: Bharathkumar S <bharath.kumar@namastecredit.com>
# Python Environment - python 3
# ==========================================================================================
try: 
    from django.shortcuts import render, redirect
    from django.contrib.auth.models import User
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.decorators import login_required
    from django.views.generic import TemplateView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.http import HttpResponse, JsonResponse
    from django.contrib import messages
    from django import forms
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    from django.contrib.auth.decorators import login_required
    from .forms import UploadFileForm
    from django.core.files.storage import FileSystemStorage
    import os
    import requests
    from lxml import html
except:
    print('error')
    pass
#*****************************************PATH SPECIFICATOION**************************************************************#
home_path = os.path.expandvars('$HOME')
#PROJECT_PATH = os.path.join(home_path, "Documents/repositories/troubleshooting_portal/")
#*****************************************END**************************************************************#

#{0}*************************[BHARATHKUMAR S]*****************************************************************#
#***************************************LOGIN SYSTEM**********************************************************#

def home(request):
    #count = User.objects.count()
    return render(request, 'index.html')


def resume(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')    

def blog(request):
    return render(request, 'blog.html')   

def flow_charts(request):
    return render(request, 'flow_chart.html')             
