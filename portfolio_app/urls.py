# ========================================================================================
# ! /usr/bin/env python
# Filename: urls.py

# Description:Adding Functionality to the WebApp

# Author: Bharathkumar S <bharath.kumar@namastecredit.com>
# Python Environment - python 3
# ==========================================================================================
from django.contrib import admin
from django.urls import path, include

from webapp import views
from webapp import forms
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('sbk_portfolio/home/', views.home, name='home'),
    path('sbk_portfolio/resume/', views.resume, name='resume'),
    path('sbk_portfolio/services/', views.services, name='services'),
    path('sbk_portfolio/portfolio/', views.portfolio, name='portfolio'),
	path('sbk_portfolio/blog/', views.blog, name='blog'),
	path ('sbk_portfolio/flow_charts/',views.flow_charts,name='flow_charts')    

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Future Reference
#path('extract/',views.extract,name = 'extract'),
#path('consolidation/',views.consolidation_home,name='consolidation'),
#path('others/',views.others,name='others'),
#path('result/',views.result,name='result'),