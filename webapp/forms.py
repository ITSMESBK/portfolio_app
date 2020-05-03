# ========================================================================================
# ! /usr/bin/env python
# Filename: forms.py

# Description: WEB APPLICATION BACKEND

# Author: Bharathkumar S <bharath.kumar@namastecredit.com>
# Python Environment - python 3
# ==========================================================================================
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()